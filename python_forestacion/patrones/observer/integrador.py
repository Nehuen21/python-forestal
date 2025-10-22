"""
Archivo integrador generado automaticamente
Directorio: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/observer
Fecha: 2025-10-22 12:08:04
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/observer/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: observable.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/observer/observable.py
# ================================================================================

from typing import Generic, TypeVar, List
from abc import ABC
from python_forestacion.patrones.observer.observer import Observer

T = TypeVar('T')

class Observable(Generic[T], ABC):
    """Clase base para objetos observables (sujetos)."""
    
    def __init__(self) -> None:
        self._observadores: List[Observer[T]] = []
    
    def agregar_observador(self, observador: Observer[T]) -> None:
        """Agrega un observador a la lista si no estaba registrado."""
        if observador not in self._observadores:
            self._observadores.append(observador)
    
    def eliminar_observador(self, observador: Observer[T]) -> None:
        """Elimina un observador de la lista si estaba registrado."""
        if observador in self._observadores:
            self._observadores.remove(observador)
    
    def notificar_observadores(self, evento: T) -> None:
        """Notifica a todos los observadores registrados con el evento."""
        for observador in self._observadores:
            try:
                observador.actualizar(evento)
            except Exception as e:
                print(f"[Observable] Error notificando observador {observador}: {e}")
    
    def get_cantidad_observadores(self) -> int:
        """Devuelve la cantidad de observadores registrados."""
        return len(self._observadores)
    
    def limpiar_observadores(self) -> None:
        """Elimina todos los observadores registrados."""
        self._observadores.clear()


# ================================================================================
# ARCHIVO 3/3: observer.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/observer/observer.py
# ================================================================================

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class Observer(Generic[T], ABC):
    """Interfaz para objetos observadores en el patrón Observer."""
    
    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """Método llamado cuando el observable notifica un cambio."""
        pass

