"""
Archivo integrador generado automaticamente
Directorio: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/cultivos
Fecha: 2025-10-22 12:08:04
Total de archivos integrados: 8
"""

# ================================================================================
# ARCHIVO 1/8: __init__.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/cultivos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/8: arbol_service.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/cultivos/arbol_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/8: cultivo_service.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/cultivos/cultivo_service.py
# ================================================================================

from abc import ABC, abstractmethod
from datetime import date
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class CultivoService(ABC):
    """Servicio base para todos los cultivos."""
    
    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        self._estrategia_absorcion = estrategia_absorcion

    def absorver_agua(self, cultivo: Cultivo, fecha: date, temperatura: float, humedad: float) -> int:
        """
        El cultivo absorbe agua según su estrategia.
        
        Returns:
            Cantidad de agua absorbida en litros
        """
        agua_absorvida = self._estrategia_absorcion.calcular_absorcion(
            fecha, temperatura, humedad, cultivo
        )
        
        # Actualizar agua del cultivo
        cultivo.set_agua(cultivo.get_agua() + agua_absorvida)
        
        return agua_absorvida

    @abstractmethod
    def mostrar_datos(self, cultivo: Cultivo) -> None:
        """Muestra los datos específicos del cultivo."""
        pass

    @abstractmethod
    def hacer_crecer(self, cultivo: Cultivo) -> None:
        """Hace crecer al cultivo (implementación específica por tipo)."""
        pass

# ================================================================================
# ARCHIVO 4/8: cultivo_service_registry.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ================================================================================

from threading import Lock
from typing import Dict, Type, Callable
from datetime import date

from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

class CultivoServiceRegistry:
    """
    Registry singleton para servicios de cultivos.
    Maneja dispatch polimórfico evitando instanceof.
    """
    
    _instance = None
    _lock = Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._init_servicios()
        return cls._instance
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance
    
    def _init_servicios(self):
        """Inicializa todos los servicios y los handlers."""
        from python_forestacion.servicios.cultivos.pino_service import PinoService
        from python_forestacion.servicios.cultivos.olivo_service import OlivoService
        from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
        from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService
        
        self._pino_srv = PinoService()
        self._olivo_srv = OlivoService()
        self._lechuga_srv = LechugaService()
        self._zanahoria_srv = ZanahoriaService()
        
        self._absorber_agua_handlers: Dict[Type[Cultivo], Callable] = {
            Pino: self._absorber_pino,
            Olivo: self._absorber_olivo,
            Lechuga: self._absorber_lechuga,
            Zanahoria: self._absorber_zanahoria
        }
        
        self._mostrar_datos_handlers: Dict[Type[Cultivo], Callable] = {
            Pino: self._mostrar_pino,
            Olivo: self._mostrar_olivo,
            Lechuga: self._mostrar_lechuga,
            Zanahoria: self._mostrar_zanahoria
        }
        
        self._hacer_crecer_handlers: Dict[Type[Cultivo], Callable] = {
            Pino: self._hacer_crecer_pino,
            Olivo: self._hacer_crecer_olivo
        }
    
    # === MÉTODOS PÚBLICOS ===
    
    def absorber_agua(self, cultivo: Cultivo, fecha: date = None, temp: float = 20.0, hum: float = 50.0) -> int:
        tipo = type(cultivo)
        if tipo not in self._absorber_agua_handlers:
            raise ValueError(f"Cultivo no registrado: {tipo}")
        return self._absorber_agua_handlers[tipo](cultivo, fecha, temp, hum)
    
    def mostrar_datos(self, cultivo: Cultivo) -> None:
        tipo = type(cultivo)
        if tipo not in self._mostrar_datos_handlers:
            raise ValueError(f"Cultivo no registrado: {tipo}")
        self._mostrar_datos_handlers[tipo](cultivo)
    
    def hacer_crecer(self, cultivo: Cultivo) -> None:
        tipo = type(cultivo)
        if tipo in self._hacer_crecer_handlers:
            self._hacer_crecer_handlers[tipo](cultivo)
    
    # === HANDLERS ===
    
    def _absorber_pino(self, cultivo: Pino, fecha: date, temp: float, hum: float) -> int:
        return self._pino_srv.absorver_agua(cultivo, fecha, temp, hum)
    
    def _mostrar_pino(self, cultivo: Pino) -> None:
        self._pino_srv.mostrar_datos(cultivo)
    
    def _hacer_crecer_pino(self, cultivo: Pino) -> None:
        self._pino_srv.hacer_crecer(cultivo)
    
    def _absorber_olivo(self, cultivo: Olivo, fecha: date, temp: float, hum: float) -> int:
        return self._olivo_srv.absorver_agua(cultivo, fecha, temp, hum)
    
    def _mostrar_olivo(self, cultivo: Olivo) -> None:
        self._olivo_srv.mostrar_datos(cultivo)
    
    def _hacer_crecer_olivo(self, cultivo: Olivo) -> None:
        self._olivo_srv.hacer_crecer(cultivo)
    
    def _absorber_lechuga(self, cultivo: Lechuga, fecha: date, temp: float, hum: float) -> int:
        return self._lechuga_srv.absorver_agua(cultivo, fecha, temp, hum)
    
    def _mostrar_lechuga(self, cultivo: Lechuga) -> None:
        self._lechuga_srv.mostrar_datos(cultivo)
    
    def _absorber_zanahoria(self, cultivo: Zanahoria, fecha: date, temp: float, hum: float) -> int:
        return self._zanahoria_srv.absorver_agua(cultivo, fecha, temp, hum)
    
    def _mostrar_zanahoria(self, cultivo: Zanahoria) -> None:
        self._zanahoria_srv.mostrar_datos(cultivo)
    
    # === MÉTODOS DE VERIFICACIÓN ===
    
    def verificar_singleton(self) -> bool:
        inst1 = CultivoServiceRegistry()
        inst2 = CultivoServiceRegistry()
        inst3 = CultivoServiceRegistry.get_instance()
        return inst1 is inst2 is inst3
    
    def get_cantidad_handlers(self) -> dict:
        return {
            "absorber_agua": len(self._absorber_agua_handlers),
            "mostrar_datos": len(self._mostrar_datos_handlers),
            "hacer_crecer": len(self._hacer_crecer_handlers),
            "tipos": list(self._absorber_agua_handlers.keys())
        }
    
    def __str__(self):
        return f"CultivoServiceRegistry({self.get_cantidad_handlers()})"
    
    __repr__ = __str__


# ================================================================================
# ARCHIVO 5/8: lechuga_service.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/cultivos/lechuga_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 6/8: olivo_service.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/cultivos/olivo_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 7/8: pino_service.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/cultivos/pino_service.py
# ================================================================================

from datetime import date
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_PINO

class PinoService(ArbolService):
    """Servicio específico para cultivos de tipo Pino."""
    
    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())
    
    def absorver_agua(self, cultivo: Pino, fecha: date, temperatura: float, humedad: float) -> int:
        """El pino absorbe agua según estrategia estacional."""
        return super().absorver_agua(cultivo, fecha, temperatura, humedad)
    
    def hacer_crecer(self, cultivo: Pino) -> None:
        """El pino crece en altura cuando se riega."""
        cultivo.crecer(CRECIMIENTO_PINO)
        print(f"Pino {cultivo.get_id()} creció a {cultivo.get_altura():.2f}m")
    
    def mostrar_datos(self, cultivo: Pino) -> None:
        """Muestra los datos específicos del pino."""
        print(f"Cultivo: Pino")
        print(f"Superficie: {cultivo.get_superficie()} m²")
        print(f"Agua almacenada: {cultivo.get_agua()} L")
        print(f"ID: {cultivo.get_id()}")
        print(f"Altura: {cultivo.get_altura():.2f} m")
        print(f"Variedad: {cultivo.get_variedad()}")
        print("-" * 20)

# ================================================================================
# ARCHIVO 8/8: zanahoria_service.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/cultivos/zanahoria_service.py
# ================================================================================

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

