"""
Constantes centralizadas del sistema PythonForestal.
NO hardcodear valores magicos en el codigo.
"""

# ===== AGRICULTURA =====
SUPERFICIE_MINIMA = 0.0
PADRON_CATASTRAL_MINIMO = 1

# ===== AGUA =====
AGUA_INICIAL_PLANTACION = 500
# Constantes para el sistema de riego
AGUA_MINIMA = 10  # Litros mínimos requeridos para regar
# ===== CULTIVOS - SUPERFICIES =====
SUPERFICIE_PINO = 2.0
SUPERFICIE_OLIVO = 3.0
SUPERFICIE_LECHUGA = 0.10
SUPERFICIE_ZANAHORIA = 0.15

# ===== CULTIVOS - AGUA INICIAL =====
AGUA_INICIAL_PINO = 2
AGUA_INICIAL_OLIVO = 5
AGUA_INICIAL_LECHUGA = 1
AGUA_INICIAL_ZANAHORIA = 0

# ===== CULTIVOS - ALTURA =====
ALTURA_INICIAL_ARBOL = 1.0

# ===== ESTRATEGIAS DE ABSORCION =====
# Estacional (Arboles)
MES_INICIO_VERANO = 3  # Marzo
MES_FIN_VERANO = 8     # Agosto
ABSORCION_SEASONAL_VERANO = 5  # Litros en verano
ABSORCION_SEASONAL_INVIERNO = 2  # Litros en invierno

# Constante (Hortalizas)
ABSORCION_CONSTANTE_LECHUGA = 1  # Litros siempre
ABSORCION_CONSTANTE_ZANAHORIA = 2  # Litros siempre

# ===== RIEGO AUTOMATIZADO =====
# Sensores
INTERVALO_SENSOR_TEMPERATURA = 2.0  # segundos
INTERVALO_SENSOR_HUMEDAD = 3.0      # segundos
INTERVALO_CONTROL_RIEGO = 2.5       # segundos

# Rangos de sensores
SENSOR_TEMP_MIN = -25  # °C
SENSOR_TEMP_MAX = 50   # °C
SENSOR_HUMEDAD_MIN = 0    # %
SENSOR_HUMEDAD_MAX = 100  # %

# Condiciones de riego
TEMP_MIN_RIEGO = 8    # °C
TEMP_MAX_RIEGO = 15   # °C
HUMEDAD_MAX_RIEGO = 50  # %

# ===== THREADING =====
THREAD_JOIN_TIMEOUT = 2.0  # segundos

# ===== PERSISTENCIA =====
DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"