from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.constantes import ABSORCION_CONSTANTE_LECHUGA

class LechugaService(CultivoService):
    """Servicio para las  operaciones que sean especificas de Lechuga."""

    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_CONSTANTE_LECHUGA))

    def mostrar_datos(self, cultivo: Lechuga) -> None:
        """Imprime información detallada de la lechuga."""
        self._imprimir_datos_base(cultivo)
        print(f"Variedad cultivada: {cultivo.get_variedad()}")
        print(f"Ubicación: {'Invernadero' if cultivo.get_invernadero() else 'Campo abierto'}")
