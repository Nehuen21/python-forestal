"""
Archivo integrador generado automaticamente
Directorio: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/factory
Fecha: 2025-10-22 12:08:04
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/factory/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: cultivo_factory.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/factory/cultivo_factory.py
# ================================================================================

from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

class CultivoFactory:
    _contador_id = 0

    @classmethod
    def _generar_id(cls) -> int:
        cls._contador_id += 1
        return cls._contador_id

    @staticmethod
    def crear_cultivo(especie: str) -> Cultivo:
        factories = {
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
        id_cultivo = CultivoFactory._generar_id()
        return Pino(id=id_cultivo, variedad="Parana")

    @staticmethod
    def _crear_olivo() -> Olivo:
        id_cultivo = CultivoFactory._generar_id()
        return Olivo(id=id_cultivo, variedad="Arbequina")

    @staticmethod
    def _crear_lechuga() -> Lechuga:
        id_cultivo = CultivoFactory._generar_id()
        return Lechuga(id=id_cultivo, variedad="Iceberg")

    @staticmethod
    def _crear_zanahoria() -> Zanahoria:
        id_cultivo = CultivoFactory._generar_id()
        return Zanahoria(id=id_cultivo, variedad="Nantes")

