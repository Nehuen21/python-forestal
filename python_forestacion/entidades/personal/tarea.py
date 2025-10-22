from dataclasses import dataclass, field
from datetime import date


@dataclass
class Tarea:
    """
    Representa una tarea asignada a un trabajador.
    Contiene información sobre la fecha, la descripción y el estado de avance.
    """

    _id_tarea: int = field(init=True, repr=False)
    _fecha_programada: date = field(init=True, repr=False)
    _descripcion: str = field(init=True, repr=False)
    _estado: str = field(default="pendiente", repr=False)

    # ---------------------------
    # Propiedades de acceso
    # ---------------------------
    @property
    def id_tarea(self) -> int:
        """Devuelve el identificador único de la tarea."""
        return self._id_tarea

    @property
    def fecha_programada(self) -> date:
        """Obtiene la fecha en la que la tarea debe realizarse."""
        return self._fecha_programada

    @fecha_programada.setter
    def fecha_programada(self, nueva_fecha: date) -> None:
        """Permite modificar la fecha de la tarea."""
        if not isinstance(nueva_fecha, date):
            raise TypeError("La fecha programada debe ser un objeto date.")
        self._fecha_programada = nueva_fecha

    @property
    def descripcion(self) -> str:
        """Obtiene la descripción de la tarea."""
        return self._descripcion

    @descripcion.setter
    def descripcion(self, nueva_descripcion: str) -> None:
        """Actualiza la descripción de la tarea, validando su contenido."""
        if not isinstance(nueva_descripcion, str):
            raise TypeError("La descripción debe ser una cadena de texto.")
        if not nueva_descripcion.strip():
            raise ValueError("La descripción no puede estar vacía.")
        self._descripcion = nueva_descripcion.strip()

    @property
    def estado(self) -> str:
        """Devuelve el estado actual de la tarea."""
        return self._estado

    # ---------------------------
    # Métodos de negocio
    # ---------------------------
    def completar(self) -> None:
        """Marca la tarea como completada."""
        self._estado = "completada"

    def reprogramar(self, nueva_fecha: date) -> None:
        """Permite reprogramar una tarea a otra fecha futura."""
        if nueva_fecha <= date.today():
            raise ValueError("La nueva fecha debe ser posterior a la actual.")
        self._fecha_programada = nueva_fecha
        self._estado = "reprogramada"

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
        return (
            f"[Tarea #{self._id_tarea}] "
            f"{self._descripcion} - Fecha: {self._fecha_programada} "
            f"({self._estado.upper()})"
        )

    def __repr__(self) -> str:
        return (
            f"Tarea(id_tarea={self._id_tarea}, "
            f"fecha_programada={self._fecha_programada}, "
            f"descripcion='{self._descripcion}', "
            f"estado='{self._estado}')"
        )
