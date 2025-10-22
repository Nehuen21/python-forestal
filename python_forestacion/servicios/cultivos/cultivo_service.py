from typing import Generic, TypeVar, List
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

T = TypeVar("T")

class CultivoService(Generic[T]):
    """Servicio genérico para manejar cultivos."""

    def __init__(self, estrategia: AbsorcionAguaStrategy = None):
        self._cultivos: List[T] = []
        self._estrategia = estrategia  # Estrategia de absorción de agua

    def agregar_cultivo(self, cultivo: T):
        self._cultivos.append(cultivo)

    def regar_cultivo(self, cultivo: T, fecha, temperatura: float, humedad: float) -> int:
        if self._estrategia:
            return self._estrategia.calcular_absorcion(cultivo, fecha, temperatura, humedad)
        return 0

    def get_cultivos(self) -> List[T]:
        return self._cultivos
