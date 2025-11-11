import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# ==========================================================
# Dataset sintético para BigQuery (costas por cuantía + fechas)
# - CUANTIA (2 decimales)
# - COSTAS  (2 decimales) con clamp [1, 50000]
# - FECHA_SENTENCIA (DATE)
# - FECHA_COBRO = FECHA_SENTENCIA + ~86 días (ruido normal)
# ==========================================================

# Parámetros del modelo base
intercepto = 415.540289
coef1 = 0.20949899

# Configuración general
n = 5000
np.random.seed(42)

# --- Rango de fechas de sentencia (ajústalo si quieres) ---
# Generaremos sentencias entre 2024-01-01 y 2025-09-30
start_date = pd.to_datetime("2024-01-01")
end_date   = pd.to_datetime("2025-09-30")
days_span  = (end_date - start_date).days

def sample_fechas(k: int):
    # elegimos días aleatorios dentro del rango
    offsets = np.random.randint(0, days_span + 1, size=k)
    return start_date + pd.to_timedelta(offsets, unit="D")

def gen_lote(m: int) -> pd.DataFrame:
    # Variables independientes
    cuantia = np.random.uniform(0, 10000, m)

    # Ruido aleatorio ±500
    ruido = np.random.uniform(-500, 500, m)

    # Costas (sin columna auxiliar)
    costas = intercepto + coef1 * cuantia + ruido

    # Fechas
    fecha_sent = sample_fechas(m)

    # Desfase ~N(86, 12) días, mínimo 1 día
    desfase = np.maximum(1, np.rint(np.random.normal(loc=86, scale=12, size=m)).astype(int))
    fecha_cobro = fecha_sent + pd.to_timedelta(desfase, unit="D")

    df_lote = pd.DataFrame({
        "CUANTIA": cuantia,
        "COSTAS": costas,
        "FECHA_SENTENCIA": fecha_sent.date,
        "FECHA_COBRO": fecha_cobro.date
    })
    # filtro de COSTAS
    df_lote = df_lote[(df_lote["COSTAS"] >= 1) & (df_lote["COSTAS"] <= 50000)]
    return df_lote

# Generamos hasta alcanzar 5000 válidas
df = gen_lote(n)
while len(df) < 5000:
    df = pd.concat([df, gen_lote(1000)], ignore_index=True)

# Limitar a 5000 exactas y redondear importes
df = df.head(5000).copy()
df["CUANTIA"] = df["CUANTIA"].round(2)
df["COSTAS"]  = df["COSTAS"].round(2)

# Guardar en CSV (con cabeceras)
output_path = "dataset_costas.csv"
df.to_csv(output_path, index=False)

print(f"✅ Dataset generado: {output_path} con {len(df)} filas")
print(df.head())
