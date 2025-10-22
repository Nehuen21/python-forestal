from python_forestacion.excepciones.forestacion_exception import ForestacionException


class AguaAgotadaException(ForestacionException):
    """Error lanzado cuando el recurso hídrico es insuficiente para regar un cultivo."""

    def __init__(self,mensaje_usuario: str,mensaje_tecnico: str,litros_disponibles: float,litros_necesarios: float,contexto: str = None,
    ):
        super().__init__(mensaje_usuario, mensaje_tecnico, contexto)
        self._litros_disponibles = litros_disponibles
        self._litros_necesarios = litros_necesarios

    def get_litros_disponibles(self) -> float:
        return self._litros_disponibles

    def get_litros_necesarios(self) -> float:
        return self._litros_necesarios

    def get_full_message(self) -> str:
        base = super().get_full_message()
        return (
            f"{base} | Agua disponible: {self._litros_disponibles:.2f}L"
            f" | Agua requerida: {self._litros_necesarios:.2f}L"
        )
