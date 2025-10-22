from dataclasses import dataclass, field


@dataclass
class Herramienta:
    """
    Representa una herramienta utilizada en tareas agrícolas o de forestación.
    Cada herramienta puede requerir un certificado de Higiene y Seguridad (HyS).
    """

    _id_herramienta: int = field(init=True, repr=False)
    _nombre: str = field(init=True, repr=False)
    _certificado_hys: bool = field(default=False, repr=False)

    # ---------------------------
    # Propiedades de acceso
    # ---------------------------
    @property
    def id_herramienta(self) -> int:
        return self._id_herramienta

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        if not isinstance(nuevo_nombre, str):
            raise TypeError("El nombre de la herramienta debe ser una cadena de texto.")
        if not nuevo_nombre.strip():
            raise ValueError("El nombre de la herramienta no puede estar vacío.")
        self._nombre = nuevo_nombre.strip()

    @property
    def certificado_hys(self) -> bool:
        return self._certificado_hys

    @certificado_hys.setter
    def certificado_hys(self, estado: bool) -> None:
        if not isinstance(estado, bool):
            raise TypeError("El valor del certificado debe ser booleano (True/False).")
        self._certificado_hys = estado

    # ---------------------------
    # Métodos de representación
    # ---------------------------
