from python_forestacion.excepciones.forestacion_exception import ForestacionException
from typing import Optional


class PersistenciaException(ForestacionException):
    """Error al guardar o recuperar datos desde almacenamiento persistente."""

    def __init__(self,mensaje_usuario: str,mensaje_tecnico: str,archivo_afectado: str,operacion: str,contexto: Optional[str] = None,
    ):
        super().__init__(mensaje_usuario, mensaje_tecnico, contexto)
        self._archivo_afectado = archivo_afectado
        self._operacion = operacion

    def get_archivo_afectado(self) -> str:
        return self._archivo_afectado

    def get_operacion(self) -> str:
        return self._operacion

    def get_full_message(self) -> str:
        base = super().get_full_message()
        return f"{base} | Archivo: {self._archivo_afectado} | Operación: {self._operacion}"
