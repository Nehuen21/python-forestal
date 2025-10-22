from typing import Generic, TypeVar, List
from python_forestacion.entidades.cultivos.cultivo import Cultivo

T = TypeVar('T', bound=Cultivo)

class Paquete(Generic[T]):
    def __init__(self, tipo_cultivo: type, cantidad: int):
        self._tipo_cultivo = tipo_cultivo
        self._cantidad = cantidad
        self._contenidos: List[T] = []

    def agregar_cultivo(self, cultivo: T):
        self._contenidos.append(cultivo)

    def mostrar_contenido_caja(self):
        print(f"Paquete de {self._tipo_cultivo.__name__}: {len(self._contenidos)} unidades")
        for c in self._contenidos:
            print(f" - {c}")
