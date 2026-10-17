# Análisis de Datos — Evento Evaluativo 3: Business Intelligence con películas

**Instituto Tecnológico Metropolitano (ITM)**
Departamento de Sistemas · Ingeniería de Sistemas
Curso: Análisis de Datos · Docente: Daniel Alexis Nieto Mora · Semestre 2026-2
Equipo 6 — Películas

## Integrantes

- Julián
- Santiago
- Oscar Alexis
- Jacobo

## Objetivo

Desarrollar un proyecto integral de Business Intelligence sobre la industria del cine: transformar los datos de TMDB en información útil para la toma de decisiones mediante hipótesis validadas estadísticamente, indicadores clave (KPIs) y un dashboard interactivo en Power BI.

*(Se completa a medida que avanza el proyecto).*

## Dataset

**TMDB 5000 Movie Dataset** — fuente secundaria publicada en Kaggle:
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

| Archivo | Contenido |
|---|---|
| `data/raw/tmdb_5000_movies.csv.zip` | 4.803 películas y 20 columnas: presupuesto, recaudación, géneros, fecha de estreno, duración, popularidad, calificación, votos, idioma, productoras y países |
| `data/raw/tmdb_5000_credits.csv.zip` | Reparto y equipo técnico de cada película |

Los archivos se dejan comprimidos tal como se descargan de Kaggle; pandas los lee directamente con `pd.read_csv`.

## Metodología

1. Comprensión del problema
2. Formulación de hipótesis
3. Preparación y modelado de datos
4. Definición de KPIs
5. Desarrollo del dashboard
6. Análisis, validación y storytelling

*(Se completa a medida que avanza el proyecto).*

## Estructura del repositorio

```text
analisis-datos-evento-3/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/          # datos originales de Kaggle
│   ├── processed/    # datos limpios y transformados
│   └── model/        # tablas de hechos y dimensiones para Power BI
├── notebooks/
│   ├── 01_comprension_problema.ipynb
│   ├── 02_preparacion_modelado.ipynb
│   ├── 03_hipotesis_pruebas.ipynb
│   ├── 04_kpis.ipynb
│   └── 05_analisis_storytelling.ipynb
├── dashboard/        # archivo de Power BI
├── images/           # capturas del dashboard y gráficas
└── docs/             # diapositivas y material del video
```

## Instalación

```bash
git clone https://github.com/JulianHZ711/analisis-datos-evento-3.git
cd analisis-datos-evento-3
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
pip install -r requirements.txt
```

Para el dashboard se necesita Power BI Desktop (gratuito, solo para Windows).

## Ejecución

Ejecutar los notebooks de la carpeta `notebooks/` en orden (01 → 05). Las rutas a los datos son relativas a esa carpeta. Luego abrir el archivo de la carpeta `dashboard/` con Power BI Desktop.

## Resultados

*(Pendiente).*

## Conclusiones

*(Pendiente).*
