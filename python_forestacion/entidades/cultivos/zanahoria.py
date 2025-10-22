from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import (
    SUPERFICIE_ZANAHORIA,
    AGUA_INICIAL_ZANAHORIA
)

class Zanahoria(Hortaliza):
    """Entidad Zanahoria - hortaliza de raíz."""

    def __init__(self, id: int, baby_carrot: bool = False):
        super().__init__(
            id=id,
            superficie=SUPERFICIE_ZANAHORIA,
            agua=AGUA_INICIAL_ZANAHORIA,
            invernadero=False  # Siempre a campo abierto según US-007
        )
        self._baby_carrot = baby_carrot

    def is_baby_carrot(self) -> bool:
        return self._baby_carrot

    def set_baby_carrot(self, baby_carrot: bool) -> None:
        self._baby_carrot = baby_carrot

    def __str__(self) -> str:
        tipo = "Baby carrot" if self._baby_carrot else "Regular"
        return (f"Zanahoria(id={self._id}, tipo='{tipo}', "
                f"superficie={self._superficie}m², agua={self._agua}L, "
                f"invernadero={self._invernadero})")

    def __repr__(self) -> str:
        return self.__str__()
