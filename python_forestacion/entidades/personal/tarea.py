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