from typing import List, TypeVar, Generic, Type
from python_forestacion.entidades.cultivos.cultivo import Cultivo

T = TypeVar('T', bound=Cultivo)

class Paquete(Generic[T]):
    """Paquete genérico tipo-seguro para empaquetar cultivos cosechados."""
    
    _contador_id = 0

    def __init__(self, tipo_cultivo: Type[T], cultivos: List[T]):
        Paquete._contador_id += 1
        self._id_paquete = Paquete._contador_id
        self._tipo_cultivo = tipo_cultivo
        self._cultivos = cultivos

    def get_id_paquete(self) -> int:
        return self._id_paquete

    def get_tipo_cultivo(self) -> Type[T]:
        return self._tipo_cultivo

    def get_cultivos(self) -> List[T]:
        return self._cultivos.copy()

    def get_cantidad(self) -> int:
        return len(self._cultivos)

    def mostrar_contenido_caja(self) -> None:
        """Muestra el contenido del paquete."""
        print(f"\n📦 Contenido de la caja #{self._id_paquete}:")
        print(f"  Tipo: {self._tipo_cultivo.__name__}")
        print(f"  Cantidad: {self.get_cantidad()}")
        print(f"  IDs de cultivos: {[c.get_id() for c in self._cultivos]}")

    def __str__(self) -> str:
        return f"Paquete(id={self._id_paquete}, tipo={self._tipo_cultivo.__name__}, cantidad={self.get_cantidad()})"

    def __repr__(self) -> str:
        return f"Paquete(id_paquete={self._id_paquete}, tipo_cultivo={self._tipo_cultivo}, cultivos={self._cultivos})"