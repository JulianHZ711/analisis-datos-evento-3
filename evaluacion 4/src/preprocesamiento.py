"""Columnas y transformaciones para modelar reservas del Evento 4."""

from sklearn.compose import ColumnTransformer
from sklearn.model_selection import StratifiedGroupKFold
from sklearn.preprocessing import OneHotEncoder, StandardScaler


SEMILLA = 42
N_PARTICIONES = 5
FRECUENCIA_MINIMA = 20
OBJETIVO = "is_canceled"
GRUPO = "grupo_perfil"
FECHAS = ("fecha_llegada", "fecha_registro_estimada")

COLUMNAS_NUMERICAS = (
    "lead_time",
    "total_noches",
    "stays_in_weekend_nights",
    "total_huespedes",
    "children",
    "babies",
    "is_repeated_guest",
    "previous_cancellations",
    "previous_bookings_not_canceled",
    "tiene_empresa",
)
COLUMNAS_CATEGORICAS = (
    "hotel",
    "mes_llegada",
    "meal",
    "market_segment",
    "distribution_channel",
    "agent",
    "reserved_room_type",
    "customer_type",
)
COLUMNAS_PREDICTORAS = COLUMNAS_NUMERICAS + COLUMNAS_CATEGORICAS


def crear_preprocesador():
    """Crea un transformador sin ajustar para el pipeline de cada modelo."""
    return ColumnTransformer(
        [
            ("numericas", StandardScaler(), list(COLUMNAS_NUMERICAS)),
            (
                "categoricas",
                OneHotEncoder(
                    min_frequency=FRECUENCIA_MINIMA,
                    handle_unknown="infrequent_if_exist",
                ),
                list(COLUMNAS_CATEGORICAS),
            ),
        ],
        remainder="drop",
    )


def crear_particionador():
    """Separa perfiles completos y procura conservar las proporciones de clase."""
    return StratifiedGroupKFold(
        n_splits=N_PARTICIONES,
        shuffle=True,
        random_state=SEMILLA,
    )
