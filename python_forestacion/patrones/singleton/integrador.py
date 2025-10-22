"""
Archivo integrador generado automaticamente
Directorio: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/singleton
Fecha: 2025-10-22 12:08:04
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/singleton/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: cultivo_service_registry.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/singleton/cultivo_service_registry.py
# ================================================================================

from threading import Lock
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.olivo_service import OlivoService
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService

class CultivoServiceRegistry:
    """Singleton Registry para dispatch polimórfico de servicios de cultivos."""

    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._inicializar_servicios()
        return cls._instance

    @classmethod
    def get_instance(cls):
        """Obtiene la instancia singleton del registry."""
        if cls._instance is None:
            cls()
        return cls._instance

    def _inicializar_servicios(self):
        """Inicializa todos los servicios y registra los handlers."""
        # Inicializar servicios
        self._pino_service = PinoService()
        self._olivo_service = OlivoService()
        self._lechuga_service = LechugaService()
        self._zanahoria_service = ZanahoriaService()

        # Registrar handlers de absorción de agua
        self._absorber_agua_handlers = {
            Pino: self._pino_service.absorver_agua,
            Olivo: self._olivo_service.absorver_agua,
            Lechuga: self._lechuga_service.absorver_agua,
            Zanahoria: self._zanahoria_service.absorver_agua
        }

        # Registrar handlers de mostrar datos
        self._mostrar_datos_handlers = {
            Pino: self._pino_service.mostrar_datos,
            Olivo: self._olivo_service.mostrar_datos,
            Lechuga: self._lechuga_service.mostrar_datos,
            Zanahoria: self._zanahoria_service.mostrar_datos
        }

        # Registrar handlers de crecimiento
        self._hacer_crecer_handlers = {
            Pino: self._pino_service.hacer_crecer,
            Olivo: self._olivo_service.hacer_crecer
            # Lechuga y Zanahoria no crecen en altura
        }

    # Métodos públicos de dispatch polimórfico
    def absorber_agua(self, cultivo, fecha=None, temperatura=20.0, humedad=50.0):
        """Hace que un cultivo absorba agua."""
        tipo = type(cultivo)
        handler = self._absorber_agua_handlers.get(tipo)
        if handler is None:
            raise ValueError(f"Tipo de cultivo no soportado: {tipo}")
        return handler(cultivo, fecha, temperatura, humedad)

    def mostrar_datos(self, cultivo):
        """Muestra los datos de un cultivo."""
        tipo = type(cultivo)
        handler = self._mostrar_datos_handlers.get(tipo)
        if handler is None:
            raise ValueError(f"Tipo de cultivo no soportado: {tipo}")
        return handler(cultivo)

    def hacer_crecer(self, cultivo):
        """Hace crecer un cultivo en altura si corresponde."""
        tipo = type(cultivo)
        handler = self._hacer_crecer_handlers.get(tipo)
        if handler:
            return handler(cultivo)
        # Si no tiene handler, no hace nada
        return None


