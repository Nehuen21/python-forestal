from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import SUPERFICIE_LECHUGA, AGUA_INICIAL_LECHUGA

class Lechuga(Hortaliza):
    def __init__(self, id: int, variedad: str = "Iceberg"):
        super().__init__(
            id=id,
            variedad=variedad,
            superficie=SUPERFICIE_LECHUGA,
            agua=AGUA_INICIAL_LECHUGA,
            invernadero=True
        )