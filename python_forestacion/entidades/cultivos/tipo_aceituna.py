from enum import Enum

class TipoAceituna(Enum):
    """Enum para los tipos de aceituna de los olivos."""
    ARBEQUINA = "Arbequina"
    PICUAL = "Picual"
    MANZANILLA = "Manzanilla"
    
    def __str__(self) -> str:
        return self.value