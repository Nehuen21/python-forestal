"""
Archivo integrador generado automaticamente
Directorio: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/terrenos
Fecha: 2025-10-22 12:08:04
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/terrenos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/terrenos/plantacion.py
# ================================================================================

from typing import List
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Plantacion:
    def __init__(self, nombre: str, superficie: float, agua: float):
        self._nombre = nombre
        self._superficie = superficie
        self._agua = agua
        self._trabajadores: List[Trabajador] = []
        self._cultivos: List[Cultivo] = []

    # ===== GETTERS =====
    def get_nombre(self) -> str:
        return self._nombre

    def get_superficie(self) -> float:
        return self._superficie

    def get_agua(self) -> float:
        return self._agua

    def get_trabajadores(self) -> List[Trabajador]:
        return self._trabajadores.copy()

    def get_cultivos(self) -> List[Cultivo]:
        return self._cultivos.copy()

    # ===== SETTERS =====
    def set_trabajadores(self, trabajadores: List[Trabajador]):
        self._trabajadores = trabajadores.copy()

    def agregar_cultivo(self, cultivo: Cultivo):
        self._cultivos.append(cultivo)

    def agregar_cultivos(self, cultivos: List[Cultivo]):
        self._cultivos.extend(cultivos)

    def remover_cultivo(self, cultivo: Cultivo):
        """Remueve un cultivo específico de la plantación."""
        if cultivo in self._cultivos:
            self._cultivos.remove(cultivo)

    # ===== OPERACIONES =====
    def descontar_agua(self, cantidad: float):
        self._agua = max(self._agua - cantidad, 0)

    def agregar_agua(self, cantidad: float):
        self._agua += cantidad

# ================================================================================
# ARCHIVO 3/4: registro_forestal.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/terrenos/registro_forestal.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/4: tierra.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/terrenos/tierra.py
# ================================================================================

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


