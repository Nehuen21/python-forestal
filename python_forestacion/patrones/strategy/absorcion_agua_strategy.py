from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionAguaStrategy(ABC):
    """Interfaz Strategy para algoritmos de absorción de agua de cultivos."""

    @abstractmethod
    def calcular_absorcion(
        self,
        cultivo: 'Cultivo',
        fecha: date,
        temperatura: float,
        humedad: float
    ) -> int:
       
        
        pass
