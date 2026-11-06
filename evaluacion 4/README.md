# Evaluación 4: predicción de cancelaciones hoteleras y segmentación de reservas

**Instituto Tecnológico Metropolitano (ITM)**
Departamento de Sistemas · Ingeniería de Sistemas
Curso: Análisis de Datos · Docente: Daniel Alexis Nieto Mora · Semestre 2026-2
Equipo 6

## Integrantes

- Julián Zapata Gutierrez
- Santiago Villada Arboleda
- Oscar Alexis Pineda Henao
- Jacobo Osorio Zapata

Igual que en el Evento 3, nos repartimos el trabajo por commits, rotando entre los cuatro.

## Descripción

Con las reservas de dos hoteles de Portugal entrenamos modelos que anticipan si una reserva se va a cancelar (aprendizaje supervisado) y agrupamos las reservas en segmentos sin usar la cancelación (aprendizaje no supervisado). Al final comparamos los dos enfoques y proponemos estrategias para que el hotel reduzca las cancelaciones o lo que le cuestan.

## Datos

**Hotel Booking Demand**, publicado en Kaggle:
https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand

Los datos originales son del artículo de Antonio, N., de Almeida, A. y Nunes, L. (2019). Hotel booking demand datasets. *Data in Brief*, 22, 41-49. https://doi.org/10.1016/j.dib.2018.11.083

| Archivo | Contenido |
|---|---|
| `data/raw/hotel_bookings.csv.zip` | 119.390 reservas y 32 columnas de un hotel de playa (Algarve) y uno de ciudad (Lisboa), con llegadas entre julio de 2015 y agosto de 2017 |

El archivo se deja comprimido tal como se descarga de Kaggle; pandas lo lee directamente con `pd.read_csv`.

## Estructura

## Ejecución

```bash
git clone https://github.com/JulianHZ711/analisis-datos-evento-3.git
cd "analisis-datos-evento-3/evaluacion 4"
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
pip install -r requirements.txt
```

Los notebooks se corren en orden desde la carpeta `notebooks/`, porque las rutas a los datos son relativas a esa carpeta.

## Resultados
