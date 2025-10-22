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
