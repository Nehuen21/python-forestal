"""
Archivo integrador generado automaticamente
Directorio: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/observer/eventos
Fecha: 2025-10-22 12:08:04
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/observer/eventos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: evento_plantacion.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/observer/eventos/evento_plantacion.py
# ================================================================================

from dataclasses import dataclass
from datetime import datetime

@dataclass
class EventoPlantacion:
    """
    Representa un evento que ocurre en una plantación.
    """
    mensaje: str
    timestamp: datetime

# ================================================================================
# ARCHIVO 3/3: evento_sensor.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/observer/eventos/evento_sensor.py
# ================================================================================

from dataclasses import dataclass
from datetime import datetime

@dataclass
class EventoSensor:
    """
    Representa un evento de lectura de un sensor.
    """
    tipo_sensor: str
    valor: float
    timestamp: datetime

