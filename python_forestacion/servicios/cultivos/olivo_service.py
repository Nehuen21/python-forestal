from datetime import date
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_OLIVO

class OlivoService(ArbolService):
    """Servicio específico para cultivos de tipo Olivo."""
    
    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())
    
    def absorver_agua(self, cultivo: Olivo, fecha: date, temperatura: float, humedad: float) -> int:
        """El olivo absorbe agua según estrategia estacional."""
        return super().absorver_agua(cultivo, fecha, temperatura, humedad)
    
    def hacer_crecer(self, cultivo: Olivo) -> None:
        """El olivo crece en altura cuando se riega."""
        cultivo.crecer(CRECIMIENTO_OLIVO)
        print(f"Olivo {cultivo.get_id()} creció a {cultivo.get_altura():.2f}m")
    
    def mostrar_datos(self, cultivo: Olivo) -> None:
        """Muestra los datos específicos del olivo."""
        print(f"Cultivo: Olivo")
        print(f"Superficie: {cultivo.get_superficie()} m²")
        print(f"Agua almacenada: {cultivo.get_agua()} L")
        print(f"ID: {cultivo.get_id()}")
        print(f"Altura: {cultivo.get_altura():.2f} m")
        print(f"Variedad: {cultivo.get_variedad()}")
        print("-" * 20)