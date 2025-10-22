from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionAguaStrategy(ABC):
    """Interfaz Strategy para algoritmos de absorción de agua."""
    
    @abstractmethod
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        """
        Calcula la cantidad de agua que absorbe un cultivo.
        
        Args:
            fecha: Fecha actual para cálculos estacionales
            temperatura: Temperatura ambiental en °C
            humedad: Humedad ambiental en %
            cultivo: El cultivo que absorbe agua
            
        Returns:
            Cantidad de agua absorbida en litros
        """
        pass