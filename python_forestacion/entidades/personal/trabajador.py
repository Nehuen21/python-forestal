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
