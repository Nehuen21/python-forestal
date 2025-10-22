from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class Observer(Generic[T], ABC):
    """Interfaz para observadores que reciben notificaciones de un Observable."""
    
    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """
        Método llamado cuando el observable notifica un cambio.
        
        Args:
            evento: Datos del evento notificado
        """
        pass
