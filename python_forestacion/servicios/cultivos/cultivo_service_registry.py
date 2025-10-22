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
