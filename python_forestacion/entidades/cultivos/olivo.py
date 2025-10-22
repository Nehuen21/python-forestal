from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
from python_forestacion.constantes import (
    SUPERFICIE_OLIVO,
    AGUA_INICIAL_OLIVO,
    ALTURA_INICIAL_ARBOL
)

class Olivo(Arbol):
    """Entidad que representa un árbol olivo."""

    def __init__(self, id: int, tipo_aceituna: TipoAceituna = TipoAceituna.ARBEQUINA):
        super().__init__(
            id=id,
            superficie=SUPERFICIE_OLIVO,
            agua=AGUA_INICIAL_OLIVO,
            altura=ALTURA_INICIAL_ARBOL
        )
        self._tipo_aceituna = tipo_aceituna

    def get_tipo_aceituna(self) -> TipoAceituna:
        return self._tipo_aceituna

    def set_tipo_aceituna(self, tipo_aceituna: TipoAceituna) -> None:
        self._tipo_aceituna = tipo_aceituna

    def __str__(self) -> str:
        return (f"Olivo(id={self._id}, tipo_aceituna={self._tipo_aceituna}, "
                f"superficie={self._superficie} m², agua={self._agua} L, "
                f"altura={self._altura} m)")

    def __repr__(self) -> str:
        return self.__str__()
