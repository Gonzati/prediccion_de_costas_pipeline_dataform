import pandas as pd
import numpy as np

# ==========================================================
# Generador de dataset de entrada para pruebas del modelo
# - CUANTIA: cuantía del procedimiento (2 decimales)
# - FECHA_SENTENCIA: fecha entre ene/2024 y dic/2025
# ==========================================================

n = 5000
np.random.seed(42)

# Rango de fechas
fecha_inicio = pd.to_datetime("2024-01-01")
fecha_fin = pd.to_datetime("2025-12-31")
rango_dias = (fecha_fin - fecha_inicio).days

# Generamos cuantías y fechas
cuantia = np.random.uniform(0, 10000, n)
offsets = np.random.randint(0, rango_dias + 1, size=n)
fecha_sentencia = fecha_inicio + pd.to_timedelta(offsets, unit="D")

# ✅ Convertimos a Series para poder usar .dt.date
df = pd.DataFrame({
    "CUANTIA": np.round(cuantia, 2),
    "FECHA_SENTENCIA": pd.Series(fecha_sentencia).dt.date
})

# Guardar CSV
output_path = "dataset_nuevos_casos.csv"
df.to_csv(output_path, index=False)

print(f"✅ Dataset generado correctamente ({len(df)} filas): {output_path}")
print(df.head())
