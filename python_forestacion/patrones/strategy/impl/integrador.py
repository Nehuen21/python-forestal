"""
Archivo integrador generado automaticamente
Directorio: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/strategy/impl
Fecha: 2025-10-22 12:08:04
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/strategy/impl/__init__.py
# ================================================================================


from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy

__all__ = [
    'AbsorcionSeasonalStrategy',
    'AbsorcionConstanteStrategy'
]

# ================================================================================
# ARCHIVO 2/3: absorcion_constante_strategy.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
# ================================================================================

from datetime import date
from typing import TYPE_CHECKING
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """Estrategia constante: siempre absorbe la misma cantidad."""
    
    def __init__(self, cantidad_constante: int):
        self._cantidad = cantidad_constante

    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        return self._cantidad  # Siempre la misma cantidad

# ================================================================================
# ARCHIVO 3/3: absorcion_seasonal_strategy.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
# ================================================================================

from datetime import date
from typing import TYPE_CHECKING
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.constantes import (
    MES_INICIO_VERANO, 
    MES_FIN_VERANO,
    ABSORCION_SEASONAL_VERANO,
    ABSORCION_SEASONAL_INVIERNO
)

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """Estrategia estacional: más agua en verano, menos en invierno."""
    
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        mes = fecha.month
        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO  # 5L en verano
        else:
            return ABSORCION_SEASONAL_INVIERNO  # 2L en invierno

