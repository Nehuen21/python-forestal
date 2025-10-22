from abc import ABC
from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Hortaliza(Cultivo, ABC):
    """Clase base abstracta para todas las hortalizas."""

    def __init__(self, id: int, superficie: float, agua: int, invernadero: bool):
        super().__init__(id, superficie, agua)
        self._invernadero = invernadero

    def get_invernadero(self) -> bool:
        return self._invernadero

    def set_invernadero(self, invernadero: bool) -> None:
        self._invernadero = invernadero
