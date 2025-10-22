"""Excepciones personalizadas del sistema forestal."""

from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.persistencia_exception import PersistenciaException
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException

__all__ = [
    "ForestacionException",
    "PersistenciaException",
    "SuperficieInsuficienteException",
    "AguaAgotadaException"
]
