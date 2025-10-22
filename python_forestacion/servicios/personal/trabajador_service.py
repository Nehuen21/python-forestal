from datetime import date
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.personal.trabajador import Trabajador
    from python_forestacion.entidades.personal.apto_medico import AptoMedico
    from python_forestacion.entidades.personal.herramienta import Herramienta

from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.apto_medico import AptoMedico
from python_forestacion.entidades.personal.tarea import Tarea


class TrabajadorService:
    """
    Servicio para operaciones relacionadas con los trabajadores.

    Permite crear, asignar aptos médicos, ejecutar tareas y verificar estados.
    """

    # ==================================================
    # CONSTRUCTOR
    # ==================================================
    def __init__(self):
        """Inicializa el servicio de gestión de trabajadores."""
        pass

    # ==================================================
    # CREACIÓN Y VALIDACIÓN
    # ==================================================
    def crear_trabajador(self,dni: int,nombre: str,tareas: List[Tarea] = None
    ) -> Trabajador:
        """
        Crea un nuevo trabajador validando los datos de entrada.

        Args:
            dni (int): DNI único del trabajador.
            nombre (str): Nombre completo del trabajador.
            tareas (List[Tarea], opcional): Lista inicial de tareas.

        Returns:
            Trabajador: Instancia del trabajador creada.

        Raises:
            ValueError: Si los datos son inválidos.
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

    # ==================================================
    # APTOS MÉDICOS
    # ==================================================
    def asignar_apto_medico(
        self,
        trabajador: Trabajador,
        apto: bool,
        fecha_emision: date,
        observaciones: str = None
    ) -> AptoMedico:
        """
        Asigna un apto médico a un trabajador.

        Args:
            trabajador (Trabajador): Trabajador al que se le asigna el apto.
            apto (bool): Estado de aptitud (True o False).
            fecha_emision (date): Fecha de emisión del apto.
            observaciones (str, opcional): Comentarios adicionales.

        Returns:
            AptoMedico: Objeto de apto médico creado y asignado.
        """
        apto_medico = AptoMedico(
            apto=apto,
            fecha_emision=fecha_emision,
            observaciones=observaciones
        )

        trabajador.set_apto_medico(apto_medico)
        print(f"🩺 Apto médico asignado a {trabajador.get_nombre()} ({'Apto' if apto else 'No apto'})")
        return apto_medico

    # ==================================================
    # TAREAS Y TRABAJO
    # ==================================================
    @staticmethod
    def _obtener_id_tarea(tarea: Tarea) -> int:
        """Método auxiliar para obtener el ID de una tarea."""
        return tarea.get_id()

    def trabajar(
        self,
        trabajador: Trabajador,
        fecha: date,
        herramienta: 'Herramienta'
    ) -> bool:
        """
        Ejecuta las tareas asignadas a un trabajador.

        Args:
            trabajador (Trabajador): Trabajador que realiza las tareas.
            fecha (date): Fecha en la que se ejecutan las tareas.
            herramienta (Herramienta): Herramienta utilizada.

        Returns:
            bool: True si pudo trabajar, False si no tiene apto médico válido.
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
        print(f"   [DEBUG] Orden de tareas: {[t.get_id() for t in tareas_ordenadas]}")

        for tarea in tareas_ordenadas:
            print(f" Realizando tarea {tarea.get_id()}: {tarea.get_descripcion()}")
            tarea.completar()

        print(f"   {len(tareas_ordenadas)} tareas completadas con éxito.")
        return True

    # ==================================================
    # ESTADO GENERAL
    # ==================================================
    def verificar_estado_trabajador(self, trabajador: Trabajador) -> dict:
        """
        Retorna un resumen del estado del trabajador.

        Args:
            trabajador (Trabajador): Trabajador a evaluar.

        Returns:
            dict: Información general del trabajador.
        """
        tareas = trabajador.get_tareas()
        tareas_pendientes = [t for t in tareas if t.esta_pendiente()]
        tareas_completadas = [t for t in tareas if not t.esta_pendiente()]

        return {"dni": trabajador.get_dni(),"nombre": trabajador.get_nombre(),"tiene_apto": trabajador.tiene_apto_medico_valido(),"apto_medico": trabajador.get_apto_medico(),"total_tareas": len(tareas),"tareas_pendientes": len(tareas_pendientes),"tareas_completadas": len(tareas_completadas)
        }
