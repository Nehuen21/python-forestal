from datetime import date
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_CONSTANTE_ZANAHORIA

class ZanahoriaService(CultivoService):
    """Servicio específico para cultivos de tipo Zanahoria."""
    
    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_CONSTANTE_ZANAHORIA))
    
    def absorver_agua(self, cultivo: Zanahoria, fecha: date, temperatura: float, humedad: float) -> int:
        """La zanahoria absorbe agua constante."""
        return super().absorver_agua(cultivo, fecha, temperatura, humedad)
    
    def hacer_crecer(self, cultivo: Zanahoria) -> None:
        """Las zanahorias no crecen en altura."""
        pass  # Las hortalizas no crecen en altura
    
    def mostrar_datos(self, cultivo: Zanahoria) -> None:
        """Muestra los datos específicos de la zanahoria."""
        print(f"Cultivo: Zanahoria")
        print(f"Superficie: {cultivo.get_superficie()} m²")
        print(f"Agua almacenada: {cultivo.get_agua()} L")
        print(f"Variedad: {cultivo.get_variedad()}")
        print(f"Invernadero: {'Sí' if cultivo.get_invernadero() else 'No'}")
        print(f"Baby Carrot: {'Sí' if cultivo.is_baby_carrot() else 'No'}")
        print("-" * 20)