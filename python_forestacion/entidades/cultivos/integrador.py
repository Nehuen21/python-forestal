"""
Archivo integrador generado automaticamente
Directorio: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/cultivos
Fecha: 2025-10-22 12:08:04
Total de archivos integrados: 9
"""

# ================================================================================
# ARCHIVO 1/9: __init__.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/cultivos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/9: arbol.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/cultivos/arbol.py
# ================================================================================

from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Arbol(Cultivo):
    def __init__(self, id: int, variedad: str, superficie: float, altura: float = 1.0, agua: float = 0.0):
        super().__init__(id, variedad)
        self._superficie = superficie
        self._altura = altura
        self._agua = agua

    # ===== GETTERS =====
    def get_superficie(self) -> float:
        return self._superficie

    def get_altura(self) -> float:
        return self._altura

    def get_agua(self) -> float:
        return self._agua

    # ===== SETTERS =====
    def set_superficie(self, superficie: float) -> None:
        self._superficie = superficie

    def set_altura(self, altura: float) -> None:
        self._altura = altura

    def set_agua(self, agua: float) -> None:
        self._agua = agua

    # ===== OPERACIONES =====
    def crecer(self, incremento: float):
        self._altura += incremento

    def absorber_agua(self, cantidad: float):
        self._agua += cantidad

# ================================================================================
# ARCHIVO 3/9: cultivo.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/cultivos/cultivo.py
# ================================================================================

from abc import ABC, abstractmethod
from typing import Any

class Cultivo(ABC):
    """Clase base abstracta para todos los cultivos."""

    def __init__(self, id: int, variedad: str = ""):
        self._id = id
        self._variedad = variedad

    # ===== GETTERS =====
    def get_id(self) -> int:
        """Retorna el ID del cultivo"""
        return self._id

    def get_variedad(self) -> str:
        """Retorna la variedad del cultivo"""
        return self._variedad

    # ===== SETTERS =====
    def set_id(self, id: int) -> None:
        self._id = id

    def set_variedad(self, variedad: str) -> None:
        self._variedad = variedad

    # ===== MÉTODOS ABSTRACTOS =====
    @abstractmethod
    def get_superficie(self) -> float:
        """Retorna la superficie ocupada por el cultivo"""
        pass

    @abstractmethod
    def get_agua(self) -> float:
        """Retorna el agua almacenada en el cultivo"""
        pass

    @abstractmethod
    def absorber_agua(self, cantidad: float) -> None:
        """El cultivo absorbe una cantidad de agua"""
        pass

# ================================================================================
# ARCHIVO 4/9: hortaliza.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/cultivos/hortaliza.py
# ================================================================================

from abc import ABC
from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Hortaliza(Cultivo, ABC):
    """Clase base abstracta para todas las hortalizas."""

    def __init__(self, id: int, variedad: str, superficie: float, agua: int, invernadero: bool):
        super().__init__(id, variedad)
        self._superficie = superficie
        self._agua = agua
        self._invernadero = invernadero

    # ===== GETTERS =====
    def get_superficie(self) -> float:
        return self._superficie

    def get_agua(self) -> float:
        return self._agua

    def get_invernadero(self) -> bool:
        return self._invernadero

    # ===== SETTERS =====
    def set_superficie(self, superficie: float) -> None:
        self._superficie = superficie

    def set_agua(self, agua: int) -> None:
        self._agua = agua

    def set_invernadero(self, invernadero: bool) -> None:
        self._invernadero = invernadero

    # ===== OPERACIONES =====
    def absorber_agua(self, cantidad: float):
        self._agua += cantidad

# ================================================================================
# ARCHIVO 5/9: lechuga.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/cultivos/lechuga.py
# ================================================================================

from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import SUPERFICIE_LECHUGA, AGUA_INICIAL_LECHUGA

class Lechuga(Hortaliza):
    def __init__(self, id: int, variedad: str = "Iceberg"):
        super().__init__(
            id=id,
            variedad=variedad,
            superficie=SUPERFICIE_LECHUGA,
            agua=AGUA_INICIAL_LECHUGA,
            invernadero=True
        )

# ================================================================================
# ARCHIVO 6/9: olivo.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/cultivos/olivo.py
# ================================================================================

# python_forestacion/entidades/cultivos/olivo.py

from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import SUPERFICIE_OLIVO, ALTURA_INICIAL_ARBOL, AGUA_INICIAL_OLIVO

class Olivo(Arbol):
    def __init__(self, id: int, variedad: str = "Arbequina"):
        super().__init__(
            id=id,
            variedad=variedad,
            superficie=SUPERFICIE_OLIVO,
            altura=ALTURA_INICIAL_ARBOL,
            agua=AGUA_INICIAL_OLIVO
        )


# ================================================================================
# ARCHIVO 7/9: pino.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/cultivos/pino.py
# ================================================================================

# python_forestacion/entidades/cultivos/pino.py

from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import SUPERFICIE_PINO, ALTURA_INICIAL_ARBOL, AGUA_INICIAL_PINO

class Pino(Arbol):
    def __init__(self, id: int, variedad: str = "Parana"):
        super().__init__(
            id=id,
            variedad=variedad,
            superficie=SUPERFICIE_PINO,
            altura=ALTURA_INICIAL_ARBOL,
            agua=AGUA_INICIAL_PINO
        )


# ================================================================================
# ARCHIVO 8/9: tipo_aceituna.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/cultivos/tipo_aceituna.py
# ================================================================================

from enum import Enum

class TipoAceituna(Enum):
    """Enum para los tipos de aceituna de los olivos."""
    ARBEQUINA = "Arbequina"
    PICUAL = "Picual"
    MANZANILLA = "Manzanilla"
    
    def __str__(self) -> str:
        return self.value

# ================================================================================
# ARCHIVO 9/9: zanahoria.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/cultivos/zanahoria.py
# ================================================================================

from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import SUPERFICIE_ZANAHORIA, AGUA_INICIAL_ZANAHORIA

class Zanahoria(Hortaliza):
    def __init__(self, id: int, variedad: str = "Nantes", baby_carrot: bool = False):
        super().__init__(
            id=id,
            variedad=variedad,
            superficie=SUPERFICIE_ZANAHORIA,
            agua=AGUA_INICIAL_ZANAHORIA,
            invernadero=False
        )
        self._baby_carrot = baby_carrot

    def is_baby_carrot(self) -> bool:
        return self._baby_carrot

    def set_baby_carrot(self, baby_carrot: bool) -> None:
        self._baby_carrot = baby_carrot

