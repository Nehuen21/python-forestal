from abc import ABC, abstractmethod
from datetime import date
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class CultivoService(ABC):
    """Servicio base para todos los cultivos."""
    
    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        self._estrategia_absorcion = estrategia_absorcion

    def absorver_agua(self, cultivo: Cultivo, fecha: date, temperatura: float, humedad: float) -> int:
        """
        El cultivo absorbe agua según su estrategia.
        
        Returns:
            Cantidad de agua absorbida en litros
        """
        agua_absorvida = self._estrategia_absorcion.calcular_absorcion(
            fecha, temperatura, humedad, cultivo
        )
        
        # Actualizar agua del cultivo
        cultivo.set_agua(cultivo.get_agua() + agua_absorvida)
        
        return agua_absorvida

    @abstractmethod
    def mostrar_datos(self, cultivo: Cultivo) -> None:
        """Muestra los datos específicos del cultivo."""
        pass

    @abstractmethod
    def hacer_crecer(self, cultivo: Cultivo) -> None:
        """Hace crecer al cultivo (implementación específica por tipo)."""
        pass