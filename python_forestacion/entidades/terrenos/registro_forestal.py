from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.tierra import Tierra
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class RegistroForestal:
    """Entidad RegistroForestal - representa un registro catastral y productivo."""

    def __init__(self,id_padron: int,tierra: 'Tierra',plantacion: 'Plantacion',propietario: str,avaluo: float
    ):
        if avaluo <= 0:
            raise ValueError("El avaluo debe ser positivo")

        self._id_padron = id_padron
        self._tierra = tierra
        self._plantacion = plantacion
        self._propietario = propietario.strip() if propietario else ""
        self._avaluo = avaluo

    # --- Getters ---
    def id_padron(self) -> int:
        return self._id_padron

    def tierra(self) -> 'Tierra':
        return self._tierra

    def plantacion(self) -> 'Plantacion':
        return self._plantacion

    def propietario(self) -> str:
        return self._propietario

    def avaluo(self) -> float:
        return self._avaluo

    # --- Setters ---
    def set_propietario(self, nuevo_propietario: str) -> None:
        if not nuevo_propietario or not nuevo_propietario.strip():
            raise ValueError("El propietario no puede estar vacío")
        self._propietario = nuevo_propietario.strip()

    def set_avaluo(self, nuevo_avaluo: float) -> None:
        if nuevo_avaluo <= 0:
            raise ValueError("El avaluo debe ser positivo")
        self._avaluo = nuevo_avaluo

    # --- Representación ---
    def __str__(self) -> str:
        return (f"RegistroForestal(padrón={self._id_padron}, propietario='{self._propietario}', "f"avaluo=${self._avaluo:,.2f})"
        )

    def __repr__(self) -> str:
        return self.__str__()
