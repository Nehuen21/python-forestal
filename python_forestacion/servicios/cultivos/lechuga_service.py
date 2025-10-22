from datetime import date
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_CONSTANTE_LECHUGA

class LechugaService(CultivoService):
    """Servicio específico para cultivos de tipo Lechuga."""
    
    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_CONSTANTE_LECHUGA))
    
    def absorver_agua(self, cultivo: Lechuga, fecha: date, temperatura: float, humedad: float) -> int:
        """La lechuga absorbe agua constante."""
        return super().absorver_agua(cultivo, fecha, temperatura, humedad)
    
    def hacer_crecer(self, cultivo: Lechuga) -> None:
        """Las lechugas no crecen en altura."""
        pass  # Las hortalizas no crecen en altura
    
    def mostrar_datos(self, cultivo: Lechuga) -> None:
        """Muestra los datos específicos de la lechuga."""
        print(f"Cultivo: Lechuga")
        print(f"Superficie: {cultivo.get_superficie()} m²")
        print(f"Agua almacenada: {cultivo.get_agua()} L")
        print(f"Variedad: {cultivo.get_variedad()}")
        print(f"Invernadero: {'Sí' if cultivo.get_invernadero() else 'No'}")
        print("-" * 20)