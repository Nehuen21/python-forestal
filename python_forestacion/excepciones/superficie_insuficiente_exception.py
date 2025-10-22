from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from forestacion_exception import ForestacionException

from python_forestacion.excepciones.forestacion_exception import ForestacionException


class SuperficieInsuficienteException(ForestacionException):
    """
    Excepción lanzada cuando no hay suficiente superficie disponible
    para agregar un nuevo cultivo o expansión.
    """

    def __init__(self,user_message: str,technical_message: str,superficie_requerida: float,superficie_disponible: float,contexto: str = None
    ):
        # Validación básica para evitar datos inconsistentes
        if superficie_requerida < 0 or superficie_disponible < 0:
            raise ValueError("Las superficies no pueden ser negativas")

        super().__init__(user_message, technical_message, contexto)
        self._superficie_requerida = superficie_requerida
        self._superficie_disponible = superficie_disponible

    def get_superficie_requerida(self) -> float:
        return self._superficie_requerida

    def get_superficie_disponible(self) -> float:
        return self._superficie_disponible

    def get_full_message(self) -> str:
        
        
    
        base = super().get_full_message()
        return (
            f"{base} | Superficie requerida: {self._superficie_requerida:.2f} m²"
            f" | Superficie disponible: {self._superficie_disponible:.2f} m²"
        )
