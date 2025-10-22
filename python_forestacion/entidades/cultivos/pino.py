from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import (
    SUPERFICIE_PINO,
    AGUA_INICIAL_PINO,
    ALTURA_INICIAL_ARBOL
)

class Pino(Arbol):
    """Entidad que representa un árbol pino forestal maderable."""

    def __init__(self, id: int, variedad: str):
        super().__init__(
            id=id,
            superficie=SUPERFICIE_PINO,
            agua=AGUA_INICIAL_PINO,
            altura=ALTURA_INICIAL_ARBOL
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        return self._variedad

    def set_variedad(self, variedad: str) -> None:
        self._variedad = variedad

    def __str__(self) -> str:
        return (f"Pino(id={self._id}, variedad='{self._variedad}', "
                f"superficie={self._superficie} m², agua={self._agua} L, "
                f"altura={self._altura} m)")

    def __repr__(self) -> str:
        return self.__str__()
