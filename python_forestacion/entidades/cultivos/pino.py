# python_forestacion/entidades/cultivos/pino.py

from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import SUPERFICIE_PINO, ALTURA_INICIAL_ARBOL, AGUA_INICIAL_PINO

class Pino(Arbol):
    def __init__(self, id: int, variedad: str = "Parana"):
        super().__init__(
            id=id,
            variedad=variedad,
            superficie=SUPERFICIE_PINO,
            altura=ALTURA_INICIAL_ARBOL,
            agua=AGUA_INICIAL_PINO
        )
