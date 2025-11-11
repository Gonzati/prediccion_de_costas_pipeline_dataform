# Predicción de Costas en Google Cloud (BigQuery + Dataform + Looker)

Repositorio orientado a portfolio que muestra la creación de un **modelo predictivo de costas** en **BigQuery**, con **automatización mediante Dataform** y **visualización en Looker**. El objetivo es ilustrar un flujo end-to-end de analítica en GCP: almacenamiento, transformación, modelado y presentación de resultados.

> Descripción original del repo: *“Creación de un modelo predictivo de costas en Big Query, automatización mediante dataform y visualización con Looker”*.

---

## 🧭 Qué demuestra este proyecto

- **Modelado en BigQuery** (capa analítica en SQL).
- **Orquestación declarativa con Dataform** (transformaciones reproducibles).
- **Visualización ejecutiva** con Looker/Looker Studio.
- Separación clara por **capas y responsabilidades** (código de BQ, pipeline de Dataform, material de visualización, utilidades en scripts).

---

## 🧱 Arquitectura (alto nivel)

- **BigQuery**: almacenamiento y consultas SQL (modelo y/o vistas).
- **Dataform**: definición del pipeline de transformaciones (tablas/vistas intermedias y finales).
- **Looker**: cuadros de mando para explorar resultados y métricas.

> La carpeta `BigQuery/` agrupa SQL y activos de DW; `dataform/pipeline_prediccion/` contiene el pipeline; `Looker/` agrupa material de visualización; `scripts/` contiene utilidades de apoyo.

---

## 📁 Estructura del repositorio
BigQuery/ # SQL y activos de BigQuery (modelo/consultas)
dataform/
└─ pipeline_prediccion/ # Acciones y definiciones de Dataform
Looker/ # Recursos para el dashboard (capturas, definiciones)
scripts/ # Scripts auxiliares (bootstrap, utilidades, etc.)
.gitignore

Autor: Angel Argibay
Linkedin: www.linkedin.com/in/ángel-argibay-cabo-842504174
