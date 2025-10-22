# python_forestacion/entidades/cultivos/olivo.py

from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import SUPERFICIE_OLIVO, ALTURA_INICIAL_ARBOL, AGUA_INICIAL_OLIVO

class Olivo(Arbol):
    def __init__(self, id: int, variedad: str = "Arbequina"):
        super().__init__(
            id=id,
            variedad=variedad,
            superficie=SUPERFICIE_OLIVO,
            altura=ALTURA_INICIAL_ARBOL,
            agua=AGUA_INICIAL_OLIVO
        )
