from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion

class Tierra:
    """Entidad Tierra - representa un terreno forestal catastrado."""

    def __init__(self,id_padron_catastral: int,superficie: float,domicilio: str,nombre_plantacion: Optional[str] = None
    ):
        if id_padron_catastral <= 0:
            raise ValueError("El ID del padrón catastral debe ser positivo")
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a 0")
        if not domicilio or not domicilio.strip():
            raise ValueError("El domicilio no puede estar vacío")

        self._id_padron_catastral = id_padron_catastral
        self._superficie = superficie
        self._domicilio = domicilio
        self._nombre_plantacion = nombre_plantacion
        self._finca: Optional['Plantacion'] = None  # Asociación con plantación (US-013, US-017)

    # --- Getters y Setters ---
    def get_id_padron_catastral(self) -> int:
        return self._id_padron_catastral

    def get_superficie(self) -> float:
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a 0")
        self._superficie = superficie

    def get_domicilio(self) -> str:
        return self._domicilio

    def set_domicilio(self, nuevo_domicilio: str) -> None:
        if not nuevo_domicilio or not nuevo_domicilio.strip():
            raise ValueError("El domicilio no puede estar vacío")
        self._domicilio = nuevo_domicilio

    def get_nombre_plantacion(self) -> Optional[str]:
        return self._nombre_plantacion

    def set_nombre_plantacion(self, nombre: str) -> None:
        self._nombre_plantacion = nombre

    def get_finca(self) -> 'Plantacion':
        """Obtiene la plantación asociada a esta tierra."""
        if self._finca is None:
            raise ValueError("No hay una plantación asociada a esta tierra")
        return self._finca

    def set_finca(self, finca: 'Plantacion') -> None:
        """Asocia una plantación a la tierra."""
        self._finca = finca

    # --- Representación textual ---
    def __str__(self) -> str:
        finca_info = (
            "sin plantación"
            if self._finca is None
            else f"con plantación: {self._finca.get_nombre()}"
        )
        return (f"Tierra(id_padron_catastral={self._id_padron_catastral}, "f"superficie={self._superficie} m², "f"domicilio='{self._domicilio}', "f"plantación='{self._nombre_plantacion}', "f"{finca_info})"
        )

    def __repr__(self) -> str:
        return self.__str__()
