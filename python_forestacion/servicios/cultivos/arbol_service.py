from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class ArbolService(CultivoService):
    """Servicio base genérico para arboles como Pino y Olivo."""
    
    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        super().__init__(estrategia_absorcion)
    
    def _imprimir_datos_arbol(self, cultivo) -> None:
        """Imprime los datos comunes y específicos de un árbol."""
        self._mostrar_datos_base(cultivo)
        print(f"Identificador: {cultivo.get_id()}")
        print(f"Altura actual: {cultivo.get_altura()} m")
