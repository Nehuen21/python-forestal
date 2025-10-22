from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class Observer(Generic[T], ABC):
    """Interfaz para objetos observadores en el patrón Observer."""
    
    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """Método llamado cuando el observable notifica un cambio."""
        pass