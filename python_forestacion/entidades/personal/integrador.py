"""
Archivo integrador generado automaticamente
Directorio: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/personal
Fecha: 2025-10-22 12:08:04
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/personal/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: apto_medico.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/personal/apto_medico.py
# ================================================================================

from datetime import date
from typing import Optional


class AptoMedico:
    """
    Representa el certificado médico de un trabajador, indicando si se encuentra apto
    para desempeñar tareas dentro del proyecto de forestación.
    """

    def __init__(self,apto: bool,fecha_emision: date,observaciones: Optional[str] = None
    ):
        if not isinstance(apto, bool):
            raise ValueError("El campo 'apto' debe ser un valor booleano (True/False).")
        if not isinstance(fecha_emision, date):
            raise ValueError("El campo 'fecha_emision' debe ser de tipo datetime.date.")

        self._apto = apto
        self._fecha_emision = fecha_emision
        self._observaciones = observaciones

    # ---------------------------
    # Métodos de acceso
    # ---------------------------
    def esta_apto(self) -> bool:
        """Indica si el trabajador se encuentra médicamente apto."""
        return self._apto

    def set_apto(self, apto: bool) -> None:
        """Actualiza el estado médico del trabajador."""
        if not isinstance(apto, bool):
            raise ValueError("El valor de 'apto' debe ser booleano.")
        self._apto = apto

    def get_fecha_emision(self) -> date:
        """Devuelve la fecha de emisión del certificado médico."""
        return self._fecha_emision

    def set_fecha_emision(self, fecha: date) -> None:
        """Permite actualizar la fecha del certificado médico."""
        if not isinstance(fecha, date):
            raise ValueError("El valor de 'fecha' debe ser una instancia de datetime.date.")
        self._fecha_emision = fecha

    def get_observaciones(self) -> Optional[str]:
        """Devuelve las observaciones médicas, si existen."""
        return self._observaciones

    def set_observaciones(self, observaciones: str) -> None:
        """Agrega o actualiza observaciones médicas relevantes."""
        if observaciones is not None and not isinstance(observaciones, str):
            raise ValueError("Las observaciones deben ser de tipo str o None.")
        self._observaciones = observaciones

  
    def __str__(self) -> str:
        estado = "APTO" if self._apto else "NO APTO"
        obs = f", observaciones='{self._observaciones}'" if self._observaciones else ""
        return f"[AptoMedico: {estado} | Fecha: {self._fecha_emision}{obs}]"

    def __repr__(self) -> str:
        return f"AptoMedico(apto={self._apto}, fecha_emision={self._fecha_emision}, observaciones={self._observaciones!r})"

  
    def esta_vencido(self, fecha_actual: date) -> bool:
        """
        Indica si el certificado médico está vencido.
        Se considera vencido si tiene más de 1 año desde su fecha de emisión.
        """
        if not isinstance(fecha_actual, date):
            raise ValueError("El parámetro 'fecha_actual' debe ser una instancia de datetime.date.")
        diferencia = (fecha_actual - self._fecha_emision).days
        return diferencia > 365


# ================================================================================
# ARCHIVO 3/5: herramienta.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/personal/herramienta.py
# ================================================================================

class Herramienta:
    """
    Representa una herramienta utilizada en tareas agrícolas o de forestación.
    Cada herramienta puede requerir un certificado de Higiene y Seguridad (HyS).
    """

    def __init__(self, id_herramienta: int, nombre: str, certificado_hys: bool = False):
        self._id_herramienta = id_herramienta
        self._nombre = nombre
        self._certificado_hys = certificado_hys

    # ---------------------------
    # Getters
    # ---------------------------
    def get_id_herramienta(self) -> int:
        return self._id_herramienta

    def get_nombre(self) -> str:
        return self._nombre

    def get_certificado_hys(self) -> bool:
        return self._certificado_hys

    # ---------------------------
    # Setters
    # ---------------------------
    def set_nombre(self, nuevo_nombre: str) -> None:
        if not isinstance(nuevo_nombre, str):
            raise TypeError("El nombre de la herramienta debe ser una cadena de texto.")
        if not nuevo_nombre.strip():
            raise ValueError("El nombre de la herramienta no puede estar vacío.")
        self._nombre = nuevo_nombre.strip()

    def set_certificado_hys(self, estado: bool) -> None:
        if not isinstance(estado, bool):
            raise TypeError("El valor del certificado debe ser booleano (True/False).")
        self._certificado_hys = estado

    # ---------------------------
    # Métodos de representación
    # ---------------------------
    def __str__(self) -> str:
        return f"Herramienta(ID: {self._id_herramienta}, Nombre: {self._nombre}, Certificado H&S: {self._certificado_hys})"

    def __repr__(self) -> str:
        return f"Herramienta(id_herramienta={self._id_herramienta}, nombre='{self._nombre}', certificado_hys={self._certificado_hys})"

# ================================================================================
# ARCHIVO 4/5: tarea.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/personal/tarea.py
# ================================================================================

class Tarea:
    """
    Representa una tarea asignada a un trabajador.
    Contiene información sobre la fecha, la descripción y el estado de avance.
    """

    def __init__(self, id_tarea: int, fecha_programada, descripcion: str):
        self._id_tarea = id_tarea
        self._fecha_programada = fecha_programada
        self._descripcion = descripcion
        self._estado = "pendiente"

    # ---------------------------
    # Getters
    # ---------------------------
    def get_id(self) -> int:
        return self._id_tarea

    def get_fecha_programada(self):
        return self._fecha_programada

    def get_descripcion(self) -> str:
        return self._descripcion

    def get_estado(self) -> str:
        return self._estado

    # ---------------------------
    # Setters
    # ---------------------------
    def set_fecha_programada(self, nueva_fecha):
        self._fecha_programada = nueva_fecha

    def set_descripcion(self, nueva_descripcion: str):
        if not nueva_descripcion.strip():
            raise ValueError("La descripción no puede estar vacía.")
        self._descripcion = nueva_descripcion.strip()

    # ---------------------------
    # Métodos de negocio
    # ---------------------------
    def completar(self) -> None:
        """Marca la tarea como completada."""
        self._estado = "completada"

    def esta_pendiente(self) -> bool:
        """Indica si la tarea aún no fue completada."""
        return self._estado == "pendiente"

    def esta_completada(self) -> bool:
        """Indica si la tarea fue finalizada."""
        return self._estado == "completada"

    # ---------------------------
    # Representación
    # ---------------------------
    def __str__(self) -> str:
        return f"[Tarea #{self._id_tarea}] {self._descripcion} - Fecha: {self._fecha_programada} ({self._estado.upper()})"

    def __repr__(self) -> str:
        return f"Tarea(id_tarea={self._id_tarea}, fecha_programada={self._fecha_programada}, descripcion='{self._descripcion}', estado='{self._estado}')"

# ================================================================================
# ARCHIVO 5/5: trabajador.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/personal/trabajador.py
# ================================================================================

from datetime import date
from typing import List
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.apto_medico import AptoMedico

class Trabajador:
    """Clase que representa a un trabajador de la finca."""

    def __init__(self, dni: int, nombre: str, tareas: List[Tarea] = None):
        self._dni = dni
        self._nombre = nombre
        self._tareas = tareas or []
        self._apto_medico: AptoMedico | None = None

    def get_dni(self) -> int:
        return self._dni

    def get_nombre(self) -> str:
        return self._nombre

    def get_tareas(self) -> List[Tarea]:
        return self._tareas

    def set_apto_medico(self, apto_medico: AptoMedico):
        self._apto_medico = apto_medico

    def get_apto_medico(self) -> AptoMedico | None:
        return self._apto_medico

    def tiene_apto_medico_valido(self) -> bool:
        """Verifica si el trabajador tiene apto médico válido."""
        if self._apto_medico is None:
            return False
        return self._apto_medico.esta_apto() and not self._apto_medico.esta_vencido(date.today())

