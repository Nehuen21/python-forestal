from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.personal.trabajador import Trabajador


class Plantacion:
    def __init__(self, nombre: str, superficie: float, agua: int):
        if superficie <= 0:
            raise ValueError("La superficie tiene que  ser mayor a cero")
        if agua < 0:
            raise ValueError("El agua no puede ser negativa")

        self._nombre = nombre
        self._superficie = superficie
        self._agua = agua
        self._cultivos: List['Cultivo'] = []
        self._trabajadores: List['Trabajador'] = []  # US-017

    # --- Nombre ---
    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor

    # --- Superficie ---
    @property
    def superficie(self) -> float:
        return self._superficie

    @superficie.setter
    def superficie(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("superficie debe ser mayor a cero")
        self._superficie = valor

    # --- Agua ---
    @property
    def agua(self) -> int:
        return self._agua

    @agua.setter
    def agua(self, valor: int) -> None:
        if valor < 0:
            raise ValueError("agua no puede ser negativa")
        self._agua = valor

    # --- Cultivos ---
    def agregar_cultivo(self, cultivo: 'Cultivo') -> None:
        """Agrega un cultivo a la plantación."""
        self._cultivos.append(cultivo)

    def agregar_cultivos(self, cultivos: List['Cultivo']) -> None:
        """Agrega múltiples cultivos."""
        self._cultivos.extend(cultivos)

    def obtener_cultivos(self) -> List['Cultivo']:
        return self._cultivos.copy()

    # --- Trabajadores ---
    def agregar_trabajador(self, trabajador: 'Trabajador') -> None:
        self._trabajadores.append(trabajador)

    def establecer_trabajadores(self, trabajadores: List['Trabajador']) -> None:
        self._trabajadores = trabajadores.copy()

    def obtener_trabajadores(self) -> List['Trabajador']:
        return self._trabajadores.copy()

    # --- Representación ---
    def __str__(self) -> str:
        return (f"Plantacion('{self._nombre}', superficie={self._superficie}m², agua={self._agua}L, "
                f"cultivos={len(self._cultivos)}, trabajadores={len(self._trabajadores)})")

    def __repr__(self) -> str:
        return self.__str__()
