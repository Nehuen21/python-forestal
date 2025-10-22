"""
Archivo integrador generado automaticamente
Directorio: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/excepciones
Fecha: 2025-10-22 12:08:04
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/excepciones/__init__.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 2/6: agua_agotada_exception.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/excepciones/agua_agotada_exception.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/6: forestacion_exception.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/excepciones/forestacion_exception.py
# ================================================================================

class ForestacionException(Exception):
    """Excepción base para errores relacionados con forestación."""
    pass


# ================================================================================
# ARCHIVO 4/6: mensaje_exception.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/excepciones/mensaje_exception.py
# ================================================================================



# ================================================================================
# ARCHIVO 5/6: persistencia_exception.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/excepciones/persistencia_exception.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 6/6: superficie_insuficiente_exception.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/excepciones/superficie_insuficiente_exception.py
# ================================================================================

from .forestacion_exception import ForestacionException

class SuperficieInsuficienteException(ForestacionException):
    """Excepción lanzada cuando la superficie disponible es insuficiente."""
    pass


