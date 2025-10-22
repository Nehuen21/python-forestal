from abc import ABC
from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Hortaliza(Cultivo, ABC):
    """Clase base abstracta para todas las hortalizas."""

    def __init__(self, id: int, variedad: str, superficie: float, agua: int, invernadero: bool):
        super().__init__(id, variedad)
        self._superficie = superficie
        self._agua = agua
        self._invernadero = invernadero

    # ===== GETTERS =====
    def get_superficie(self) -> float:
        return self._superficie

    def get_agua(self) -> float:
        return self._agua

    def get_invernadero(self) -> bool:
        return self._invernadero

    # ===== SETTERS =====
    def set_superficie(self, superficie: float) -> None:
        self._superficie = superficie

    def set_agua(self, agua: int) -> None:
        self._agua = agua

    def set_invernadero(self, invernadero: bool) -> None:
        self._invernadero = invernadero

    # ===== OPERACIONES =====
    def absorber_agua(self, cantidad: float):
        self._agua += cantidad