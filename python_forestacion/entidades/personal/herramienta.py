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