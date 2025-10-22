from typing import List
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Plantacion:
    def __init__(self, nombre: str, superficie: float, agua: float):
        self._nombre = nombre
        self._superficie = superficie
        self._agua = agua
        self._trabajadores: List[Trabajador] = []
        self._cultivos: List[Cultivo] = []

    # ===== GETTERS =====
    def get_nombre(self) -> str:
        return self._nombre

    def get_superficie(self) -> float:
        return self._superficie

    def get_agua(self) -> float:
        return self._agua

    def get_trabajadores(self) -> List[Trabajador]:
        return self._trabajadores.copy()

    def get_cultivos(self) -> List[Cultivo]:
        return self._cultivos.copy()

    # ===== SETTERS =====
    def set_trabajadores(self, trabajadores: List[Trabajador]):
        self._trabajadores = trabajadores.copy()

    def agregar_cultivo(self, cultivo: Cultivo):
        self._cultivos.append(cultivo)

    def agregar_cultivos(self, cultivos: List[Cultivo]):
        self._cultivos.extend(cultivos)

    def remover_cultivo(self, cultivo: Cultivo):
        """Remueve un cultivo específico de la plantación."""
        if cultivo in self._cultivos:
            self._cultivos.remove(cultivo)

    # ===== OPERACIONES =====
    def descontar_agua(self, cantidad: float):
        self._agua = max(self._agua - cantidad, 0)

    def agregar_agua(self, cantidad: float):
        self._agua += cantidad