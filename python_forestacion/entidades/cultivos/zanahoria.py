from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import SUPERFICIE_ZANAHORIA, AGUA_INICIAL_ZANAHORIA

class Zanahoria(Hortaliza):
    def __init__(self, id: int, variedad: str = "Nantes", baby_carrot: bool = False):
        super().__init__(
            id=id,
            variedad=variedad,
            superficie=SUPERFICIE_ZANAHORIA,
            agua=AGUA_INICIAL_ZANAHORIA,
            invernadero=False
        )
        self._baby_carrot = baby_carrot

    def is_baby_carrot(self) -> bool:
        return self._baby_carrot

    def set_baby_carrot(self, baby_carrot: bool) -> None:
        self._baby_carrot = baby_carrot