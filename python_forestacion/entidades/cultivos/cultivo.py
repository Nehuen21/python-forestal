from abc import ABC, abstractmethod
from typing import Any

class Cultivo(ABC):
    """Clase base abstracta para todos los cultivos."""

    def __init__(self, id: int, variedad: str = ""):
        self._id = id
        self._variedad = variedad

    # ===== GETTERS =====
    def get_id(self) -> int:
        """Retorna el ID del cultivo"""
        return self._id

    def get_variedad(self) -> str:
        """Retorna la variedad del cultivo"""
        return self._variedad

    # ===== SETTERS =====
    def set_id(self, id: int) -> None:
        self._id = id

    def set_variedad(self, variedad: str) -> None:
        self._variedad = variedad

    # ===== MÉTODOS ABSTRACTOS =====
    @abstractmethod
    def get_superficie(self) -> float:
        """Retorna la superficie ocupada por el cultivo"""
        pass

    @abstractmethod
    def get_agua(self) -> float:
        """Retorna el agua almacenada en el cultivo"""
        pass

    @abstractmethod
    def absorber_agua(self, cantidad: float) -> None:
        """El cultivo absorbe una cantidad de agua"""
        pass