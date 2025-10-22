from datetime import date
from typing import TYPE_CHECKING
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """Estrategia de absorción de agua constante para hortalizas (Lechuga, Zanahoria)."""

    def __init__(self, cantidad_constante: int):
        """
        Inicializa la estrategia con una cantidad fija de agua.

        Args:
            cantidad_constante (int): Cantidad fija de agua a absorber (litros).
        """
        self._cantidad_constante = cantidad_constante

    def calcular_absorcion(self,cultivo: 'Cultivo',fecha: date,temperatura: float,humedad: float
    ) -> int:
       
        return self._cantidad_constante
