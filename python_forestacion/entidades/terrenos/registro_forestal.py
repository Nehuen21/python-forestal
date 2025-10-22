from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion

class RegistroForestal:
    """Representa un registro forestal completo que vincula terreno, plantacion, propietario y avaluo."""

    def __init__(self, id_padron: int, tierra: Tierra, plantacion: Plantacion, propietario: str, avaluo: float):
        self._id_padron = id_padron
        self._tierra = tierra
        self._plantacion = plantacion
        self._propietario = propietario
        self._avaluo = avaluo

    # ===== GETTERS =====
    def get_id_padron(self) -> int:
        return self._id_padron

    def get_tierra(self) -> Tierra:
        return self._tierra

    def get_plantacion(self) -> Plantacion:
        return self._plantacion

    def get_propietario(self) -> str:
        return self._propietario

    def get_avaluo(self) -> float:
        return self._avaluo

    # ===== SETTERS =====
    def set_tierra(self, tierra: Tierra) -> None:
        self._tierra = tierra

    def set_plantacion(self, plantacion: Plantacion) -> None:
        self._plantacion = plantacion

    def set_propietario(self, propietario: str) -> None:
        self._propietario = propietario

    def set_avaluo(self, avaluo: float) -> None:
        self._avaluo = avaluo

    # ===== REPRESENTACION =====
    def __str__(self) -> str:
        return f"RegistroForestal(padron={self._id_padron}, propietario='{self._propietario}', avaluo={self._avaluo})"

    def __repr__(self) -> str:
        return f"RegistroForestal(id_padron={self._id_padron}, tierra={self._tierra}, plantacion={self._plantacion}, propietario='{self._propietario}', avaluo={self._avaluo})"