"""
Archivo integrador generado automaticamente
Directorio: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/personal
Fecha: 2025-10-22 12:08:04
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/personal/__init__.py
# ================================================================================

"""Servicios relacionados con la gestión de personal y tareas de campo."""

from python_forestacion.servicios.personal.trabajador_service import TrabajadorService

__all__ = ["TrabajadorService"]


# ================================================================================
# ARCHIVO 2/2: trabajador_service.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/personal/trabajador_service.py
# ================================================================================

from datetime import date
from typing import List
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.apto_medico import AptoMedico
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.herramienta import Herramienta

class TrabajadorService:
    """
    Servicio para operaciones relacionadas con los trabajadores.
    Permite crear, asignar aptos médicos, ejecutar tareas y verificar estados.
    """

    def __init__(self):
        """Inicializa el servicio de gestión de trabajadores."""
        pass

    def crear_trabajador(self, dni: int, nombre: str, tareas: List[Tarea] = None) -> Trabajador:
        """
        Crea un nuevo trabajador validando los datos de entrada.
        """
        self._validar_datos_trabajador(dni, nombre)

        trabajador = Trabajador(
            dni=dni,
            nombre=nombre,
            tareas=tareas if tareas is not None else []
        )

        print(f"👷 Trabajador creado: {trabajador.get_nombre()} (DNI: {trabajador.get_dni()})")
        return trabajador

    def _validar_datos_trabajador(self, dni: int, nombre: str) -> None:
        """Valida los datos de entrada al crear un trabajador."""
        if not isinstance(dni, int):
            raise ValueError("El DNI debe ser un número entero")
        if dni <= 0:
            raise ValueError("El DNI debe ser un número positivo")
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

    def asignar_apto_medico(self, trabajador: Trabajador, apto: bool, fecha_emision: date, observaciones: str = None) -> AptoMedico:
        """
        Asigna un apto médico a un trabajador.
        """
        apto_medico = AptoMedico(
            apto=apto,
            fecha_emision=fecha_emision,
            observaciones=observaciones
        )

        trabajador.set_apto_medico(apto_medico)
        print(f"🩺 Apto médico asignado a {trabajador.get_nombre()} ({'Apto' if apto else 'No apto'})")
        return apto_medico

    @staticmethod
    def _obtener_id_tarea(tarea: Tarea) -> int:
        """Método auxiliar para obtener el ID de una tarea."""
        return tarea.get_id()

    def trabajar(self, trabajador: Trabajador, fecha: date, herramienta: Herramienta) -> bool:
        """
        Ejecuta las tareas asignadas a un trabajador.
        """
        if not trabajador.tiene_apto_medico_valido():
            print(f"  {trabajador.get_nombre()} no puede trabajar: sin apto médico válido.")
            return False

        tareas_del_dia = [
            t for t in trabajador.get_tareas()
            if t.get_fecha_programada() == fecha and t.esta_pendiente()
        ]

        if not tareas_del_dia:
            print(f"  {trabajador.get_nombre()} no tiene tareas pendientes para {fecha}.")
            return True

        # Ordenar tareas por ID descendente (US-016)
        tareas_ordenadas = sorted(
            tareas_del_dia,
            key=self._obtener_id_tarea,
            reverse=True
        )

        print(f" {trabajador.get_nombre()} trabajando con {herramienta.get_nombre()}...")

        for tarea in tareas_ordenadas:
            print(f" Realizando tarea {tarea.get_id()}: {tarea.get_descripcion()}")
            tarea.completar()

        print(f"   {len(tareas_ordenadas)} tareas completadas con éxito.")
        return True

    def verificar_estado_trabajador(self, trabajador: Trabajador) -> dict:
        """
        Retorna un resumen del estado del trabajador.
        """
        tareas = trabajador.get_tareas()
        tareas_pendientes = [t for t in tareas if t.esta_pendiente()]
        tareas_completadas = [t for t in tareas if not t.esta_pendiente()]

        return {
            "dni": trabajador.get_dni(),
            "nombre": trabajador.get_nombre(),
            "tiene_apto": trabajador.tiene_apto_medico_valido(),
            "apto_medico": trabajador.get_apto_medico(),
            "total_tareas": len(tareas),
            "tareas_pendientes": len(tareas_pendientes),
            "tareas_completadas": len(tareas_completadas)
        }

