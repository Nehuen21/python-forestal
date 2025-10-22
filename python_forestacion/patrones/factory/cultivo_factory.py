from typing import Type
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna


class CultivoFactory:
    """Factory Method para crear cultivos con IDs únicos."""

    _ultimo_id: int = 0  # Contador para IDs únicos

    @classmethod
    def _obtener_nuevo_id(cls) -> int:
        """Genera un nuevo ID único para cultivos."""
        cls._ultimo_id += 1
        return cls._ultimo_id

    @staticmethod
    def crear_cultivo(especie: str) -> Cultivo:
        """
        Crea un cultivo del tipo especificado.

        Args:
            especie: Tipo de cultivo ("Pino", "Olivo", "Lechuga", "Zanahoria")

        Returns:
            Cultivo: Instancia del cultivo creado

        Raises:
            ValueError: Si la especie es desconocida
        """
        factories: dict[str, callable[[], Cultivo]] = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria
        }

        if especie not in factories:
            raise ValueError(f"Especie desconocida: {especie}")

        return factories[especie]()

    @staticmethod
    def _crear_pino() -> Pino:
        """Crea un Pino con variedad por defecto."""
        id = CultivoFactory._obtener_nuevo_id()
        return Pino(id=id, variedad="Parana")

    @staticmethod
    def _crear_olivo() -> Olivo:
        """Crea un Olivo con tipo de aceituna por defecto."""
        id = CultivoFactory._obtener_nuevo_id()
        return Olivo(id=id, tipo_aceituna=TipoAceituna.ARBEQUINA)

    @staticmethod
    def _crear_lechuga() -> Lechuga:
        """Crea una Lechuga con variedad por defecto."""
        id = CultivoFactory._obtener_nuevo_id()
        return Lechuga(id=id, variedad="Crespa")

    @staticmethod
    def _crear_zanahoria() -> Zanahoria:
        """Crea una Zanahoria (regular por defecto)."""
        id = CultivoFactory._obtener_nuevo_id()
        return Zanahoria(id=id, baby_carrot=False)
