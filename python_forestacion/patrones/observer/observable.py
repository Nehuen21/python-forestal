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
