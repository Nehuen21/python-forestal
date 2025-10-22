from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import (
    SUPERFICIE_LECHUGA,
    AGUA_INICIAL_LECHUGA
)

class Lechuga(Hortaliza):
    """Entidad que representa una planta de lechuga."""

    def __init__(self, id: int, variedad: str):
        super().__init__(
            id=id,
            superficie=SUPERFICIE_LECHUGA,
            agua=AGUA_INICIAL_LECHUGA,
            invernadero=True  # Según US-006: siempre cultivada bajo invernadero
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        return self._variedad

    def set_variedad(self, variedad: str) -> None:
        self._variedad = variedad

    def __str__(self) -> str:
        return (f"Lechuga(id={self._id}, variedad='{self._variedad}', "
                f"superficie={self._superficie} m², agua={self._agua} L, "
                f"invernadero={self._invernadero})")

    def __repr__(self) -> str:
        return self.__str__()

