"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion
Fecha de generacion: 2025-10-22 12:08:04
Total de archivos integrados: 66
Total de directorios procesados: 20
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. __init__.py
#   2. constantes.py
#
# DIRECTORIO: entidades/cultivos
#   3. __init__.py
#   4. arbol.py
#   5. cultivo.py
#   6. hortaliza.py
#   7. lechuga.py
#   8. olivo.py
#   9. pino.py
#   10. tipo_aceituna.py
#   11. zanahoria.py
#
# DIRECTORIO: entidades/personal
#   12. __init__.py
#   13. apto_medico.py
#   14. herramienta.py
#   15. tarea.py
#   16. trabajador.py
#
# DIRECTORIO: entidades/terrenos
#   17. __init__.py
#   18. plantacion.py
#   19. registro_forestal.py
#   20. tierra.py
#
# DIRECTORIO: excepciones
#   21. __init__.py
#   22. agua_agotada_exception.py
#   23. forestacion_exception.py
#   24. mensaje_exception.py
#   25. persistencia_exception.py
#   26. superficie_insuficiente_exception.py
#
# DIRECTORIO: patrones
#   27. __init__.py
#
# DIRECTORIO: patrones/factory
#   28. __init__.py
#   29. cultivo_factory.py
#
# DIRECTORIO: patrones/observer
#   30. __init__.py
#   31. observable.py
#   32. observer.py
#
# DIRECTORIO: patrones/observer/eventos
#   33. __init__.py
#   34. evento_plantacion.py
#   35. evento_sensor.py
#
# DIRECTORIO: patrones/singleton
#   36. __init__.py
#   37. cultivo_service_registry.py
#
# DIRECTORIO: patrones/strategy
#   38. __init__.py
#   39. absorcion_agua_strategy.py
#
# DIRECTORIO: patrones/strategy/impl
#   40. __init__.py
#   41. absorcion_constante_strategy.py
#   42. absorcion_seasonal_strategy.py
#
# DIRECTORIO: riego
#   43. __init__.py
#
# DIRECTORIO: riego/control
#   44. __init__.py
#   45. control_riego_task.py
#
# DIRECTORIO: riego/sensores
#   46. __init__.py
#   47. humedad_reader_task.py
#   48. temperatura_reader_task.py
#
# DIRECTORIO: servicios
#   49. __init__.py
#
# DIRECTORIO: servicios/cultivos
#   50. __init__.py
#   51. arbol_service.py
#   52. cultivo_service.py
#   53. cultivo_service_registry.py
#   54. lechuga_service.py
#   55. olivo_service.py
#   56. pino_service.py
#   57. zanahoria_service.py
#
# DIRECTORIO: servicios/negocio
#   58. __init__.py
#   59. fincas_service.py
#   60. paquete.py
#
# DIRECTORIO: servicios/personal
#   61. __init__.py
#   62. trabajador_service.py
#
# DIRECTORIO: servicios/terrenos
#   63. __init__.py
#   64. plantacion_service.py
#   65. registro_forestal_service.py
#   66. tierra_service.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/66: __init__.py
# Directorio: .
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 2/66: constantes.py
# Directorio: .
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/constantes.py
# ==============================================================================

"""
Constantes centralizadas del sistema PythonForestal.
NO hardcodear valores magicos en el codigo.
"""

# ===== AGRICULTURA =====
SUPERFICIE_MINIMA = 0.0
PADRON_CATASTRAL_MINIMO = 1

# ===== AGUA =====
AGUA_INICIAL_PLANTACION = 500
AGUA_MINIMA = 10  # Litros mínimos requeridos para regar

# ===== CULTIVOS - SUPERFICIES =====
SUPERFICIE_PINO = 2.0
SUPERFICIE_OLIVO = 3.0
SUPERFICIE_LECHUGA = 0.10
SUPERFICIE_ZANAHORIA = 0.15

# ===== CULTIVOS - AGUA INICIAL =====
AGUA_INICIAL_PINO = 2
AGUA_INICIAL_OLIVO = 5
AGUA_INICIAL_LECHUGA = 1
AGUA_INICIAL_ZANAHORIA = 0

# ===== CULTIVOS - ALTURA =====
ALTURA_INICIAL_ARBOL = 1.0

# ===== CULTIVOS - CRECIMIENTO =====
CRECIMIENTO_PINO = 0.10    # metros por riego
CRECIMIENTO_OLIVO = 0.01   # metros por riego

# ===== ESTRATEGIAS DE ABSORCION =====
# Estacional (Arboles)
MES_INICIO_VERANO = 3  # Marzo
MES_FIN_VERANO = 8     # Agosto
ABSORCION_SEASONAL_VERANO = 5  # Litros en verano
ABSORCION_SEASONAL_INVIERNO = 2  # Litros en invierno

# Constante (Hortalizas)
ABSORCION_CONSTANTE_LECHUGA = 1  # Litros siempre
ABSORCION_CONSTANTE_ZANAHORIA = 2  # Litros siempre

# ===== RIEGO AUTOMATIZADO =====
# Sensores
INTERVALO_SENSOR_TEMPERATURA = 2.0  # segundos
INTERVALO_SENSOR_HUMEDAD = 3.0      # segundos
INTERVALO_CONTROL_RIEGO = 2.5       # segundos

# Rangos de sensores
SENSOR_TEMP_MIN = -25  # °C
SENSOR_TEMP_MAX = 50   # °C
SENSOR_HUMEDAD_MIN = 0    # %
SENSOR_HUMEDAD_MAX = 100  # %

# Condiciones de riego
TEMP_MIN_RIEGO = 8    # °C
TEMP_MAX_RIEGO = 15   # °C
HUMEDAD_MAX_RIEGO = 50  # %

# ===== THREADING =====
THREAD_JOIN_TIMEOUT = 2.0  # segundos

# ===== PERSISTENCIA =====
DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"


################################################################################
# DIRECTORIO: entidades/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 3/66: __init__.py
# Directorio: entidades/cultivos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/cultivos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 4/66: arbol.py
# Directorio: entidades/cultivos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/cultivos/arbol.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 5/66: cultivo.py
# Directorio: entidades/cultivos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/cultivos/cultivo.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 6/66: hortaliza.py
# Directorio: entidades/cultivos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/cultivos/hortaliza.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 7/66: lechuga.py
# Directorio: entidades/cultivos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/cultivos/lechuga.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 8/66: olivo.py
# Directorio: entidades/cultivos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/cultivos/olivo.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 9/66: pino.py
# Directorio: entidades/cultivos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/cultivos/pino.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 10/66: tipo_aceituna.py
# Directorio: entidades/cultivos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/cultivos/tipo_aceituna.py
# ==============================================================================

from enum import Enum

class TipoAceituna(Enum):
    """Enum para los tipos de aceituna de los olivos."""
    ARBEQUINA = "Arbequina"
    PICUAL = "Picual"
    MANZANILLA = "Manzanilla"
    
    def __str__(self) -> str:
        return self.value

# ==============================================================================
# ARCHIVO 11/66: zanahoria.py
# Directorio: entidades/cultivos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/cultivos/zanahoria.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: entidades/personal
################################################################################

# ==============================================================================
# ARCHIVO 12/66: __init__.py
# Directorio: entidades/personal
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/personal/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 13/66: apto_medico.py
# Directorio: entidades/personal
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/personal/apto_medico.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 14/66: herramienta.py
# Directorio: entidades/personal
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/personal/herramienta.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 15/66: tarea.py
# Directorio: entidades/personal
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/personal/tarea.py
# ==============================================================================

class Tarea:
    """
    Representa una tarea asignada a un trabajador.
    Contiene información sobre la fecha, la descripción y el estado de avance.
    """

    def __init__(self, id_tarea: int, fecha_programada, descripcion: str):
        self._id_tarea = id_tarea
        self._fecha_programada = fecha_programada
        self._descripcion = descripcion
        self._estado = "pendiente"

    # ---------------------------
    # Getters
    # ---------------------------
    def get_id(self) -> int:
        return self._id_tarea

    def get_fecha_programada(self):
        return self._fecha_programada

    def get_descripcion(self) -> str:
        return self._descripcion

    def get_estado(self) -> str:
        return self._estado

    # ---------------------------
    # Setters
    # ---------------------------
    def set_fecha_programada(self, nueva_fecha):
        self._fecha_programada = nueva_fecha

    def set_descripcion(self, nueva_descripcion: str):
        if not nueva_descripcion.strip():
            raise ValueError("La descripción no puede estar vacía.")
        self._descripcion = nueva_descripcion.strip()

    # ---------------------------
    # Métodos de negocio
    # ---------------------------
    def completar(self) -> None:
        """Marca la tarea como completada."""
        self._estado = "completada"

    def esta_pendiente(self) -> bool:
        """Indica si la tarea aún no fue completada."""
        return self._estado == "pendiente"

    def esta_completada(self) -> bool:
        """Indica si la tarea fue finalizada."""
        return self._estado == "completada"

    # ---------------------------
    # Representación
    # ---------------------------
    def __str__(self) -> str:
        return f"[Tarea #{self._id_tarea}] {self._descripcion} - Fecha: {self._fecha_programada} ({self._estado.upper()})"

    def __repr__(self) -> str:
        return f"Tarea(id_tarea={self._id_tarea}, fecha_programada={self._fecha_programada}, descripcion='{self._descripcion}', estado='{self._estado}')"

# ==============================================================================
# ARCHIVO 16/66: trabajador.py
# Directorio: entidades/personal
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/personal/trabajador.py
# ==============================================================================

from datetime import date
from typing import List
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.apto_medico import AptoMedico

class Trabajador:
    """Clase que representa a un trabajador de la finca."""

    def __init__(self, dni: int, nombre: str, tareas: List[Tarea] = None):
        self._dni = dni
        self._nombre = nombre
        self._tareas = tareas or []
        self._apto_medico: AptoMedico | None = None

    def get_dni(self) -> int:
        return self._dni

    def get_nombre(self) -> str:
        return self._nombre

    def get_tareas(self) -> List[Tarea]:
        return self._tareas

    def set_apto_medico(self, apto_medico: AptoMedico):
        self._apto_medico = apto_medico

    def get_apto_medico(self) -> AptoMedico | None:
        return self._apto_medico

    def tiene_apto_medico_valido(self) -> bool:
        """Verifica si el trabajador tiene apto médico válido."""
        if self._apto_medico is None:
            return False
        return self._apto_medico.esta_apto() and not self._apto_medico.esta_vencido(date.today())


################################################################################
# DIRECTORIO: entidades/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 17/66: __init__.py
# Directorio: entidades/terrenos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/terrenos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 18/66: plantacion.py
# Directorio: entidades/terrenos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/terrenos/plantacion.py
# ==============================================================================

from typing import List
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Plantacion:
    def __init__(self, nombre: str, superficie: float, agua: float):
        self._nombre = nombre
        self._superficie = superficie
        self._agua = agua
        self._trabajadores: List[Trabajador] = []
        self._cultivos: List[Cultivo] = []

    # ===== GETTERS =====
    def get_nombre(self) -> str:
        return self._nombre

    def get_superficie(self) -> float:
        return self._superficie

    def get_agua(self) -> float:
        return self._agua

    def get_trabajadores(self) -> List[Trabajador]:
        return self._trabajadores.copy()

    def get_cultivos(self) -> List[Cultivo]:
        return self._cultivos.copy()

    # ===== SETTERS =====
    def set_trabajadores(self, trabajadores: List[Trabajador]):
        self._trabajadores = trabajadores.copy()

    def agregar_cultivo(self, cultivo: Cultivo):
        self._cultivos.append(cultivo)

    def agregar_cultivos(self, cultivos: List[Cultivo]):
        self._cultivos.extend(cultivos)

    def remover_cultivo(self, cultivo: Cultivo):
        """Remueve un cultivo específico de la plantación."""
        if cultivo in self._cultivos:
            self._cultivos.remove(cultivo)

    # ===== OPERACIONES =====
    def descontar_agua(self, cantidad: float):
        self._agua = max(self._agua - cantidad, 0)

    def agregar_agua(self, cantidad: float):
        self._agua += cantidad

# ==============================================================================
# ARCHIVO 19/66: registro_forestal.py
# Directorio: entidades/terrenos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/terrenos/registro_forestal.py
# ==============================================================================

from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion

class RegistroForestal:
    """Representa un registro forestal completo que vincula terreno, plantacion, propietario y avaluo."""

    def __init__(self, id_padron: int, tierra: Tierra, plantacion: Plantacion, propietario: str, avaluo: float):
        self._id_padron = id_padron
        self._tierra = tierra
        self._plantacion = plantacion
        self._propietario = propietario
        self._avaluo = avaluo

    # ===== GETTERS =====
    def get_id_padron(self) -> int:
        return self._id_padron

    def get_tierra(self) -> Tierra:
        return self._tierra

    def get_plantacion(self) -> Plantacion:
        return self._plantacion

    def get_propietario(self) -> str:
        return self._propietario

    def get_avaluo(self) -> float:
        return self._avaluo

    # ===== SETTERS =====
    def set_tierra(self, tierra: Tierra) -> None:
        self._tierra = tierra

    def set_plantacion(self, plantacion: Plantacion) -> None:
        self._plantacion = plantacion

    def set_propietario(self, propietario: str) -> None:
        self._propietario = propietario

    def set_avaluo(self, avaluo: float) -> None:
        self._avaluo = avaluo

    # ===== REPRESENTACION =====
    def __str__(self) -> str:
        return f"RegistroForestal(padron={self._id_padron}, propietario='{self._propietario}', avaluo={self._avaluo})"

    def __repr__(self) -> str:
        return f"RegistroForestal(id_padron={self._id_padron}, tierra={self._tierra}, plantacion={self._plantacion}, propietario='{self._propietario}', avaluo={self._avaluo})"

# ==============================================================================
# ARCHIVO 20/66: tierra.py
# Directorio: entidades/terrenos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/entidades/terrenos/tierra.py
# ==============================================================================

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion

class Tierra:
    """Entidad Tierra - representa un terreno forestal catastrado."""

    def __init__(self,id_padron_catastral: int,superficie: float,domicilio: str,nombre_plantacion: Optional[str] = None
    ):
        if id_padron_catastral <= 0:
            raise ValueError("El ID del padrón catastral debe ser positivo")
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a 0")
        if not domicilio or not domicilio.strip():
            raise ValueError("El domicilio no puede estar vacío")

        self._id_padron_catastral = id_padron_catastral
        self._superficie = superficie
        self._domicilio = domicilio
        self._nombre_plantacion = nombre_plantacion
        self._finca: Optional['Plantacion'] = None  # Asociación con plantación (US-013, US-017)

    # --- Getters y Setters ---
    def get_id_padron_catastral(self) -> int:
        return self._id_padron_catastral

    def get_superficie(self) -> float:
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a 0")
        self._superficie = superficie

    def get_domicilio(self) -> str:
        return self._domicilio

    def set_domicilio(self, nuevo_domicilio: str) -> None:
        if not nuevo_domicilio or not nuevo_domicilio.strip():
            raise ValueError("El domicilio no puede estar vacío")
        self._domicilio = nuevo_domicilio

    def get_nombre_plantacion(self) -> Optional[str]:
        return self._nombre_plantacion

    def set_nombre_plantacion(self, nombre: str) -> None:
        self._nombre_plantacion = nombre

    def get_finca(self) -> 'Plantacion':
        """Obtiene la plantación asociada a esta tierra."""
        if self._finca is None:
            raise ValueError("No hay una plantación asociada a esta tierra")
        return self._finca

    def set_finca(self, finca: 'Plantacion') -> None:
        """Asocia una plantación a la tierra."""
        self._finca = finca

    # --- Representación textual ---
    def __str__(self) -> str:
        finca_info = (
            "sin plantación"
            if self._finca is None
            else f"con plantación: {self._finca.get_nombre()}"
        )
        return (f"Tierra(id_padron_catastral={self._id_padron_catastral}, "f"superficie={self._superficie} m², "f"domicilio='{self._domicilio}', "f"plantación='{self._nombre_plantacion}', "f"{finca_info})"
        )

    def __repr__(self) -> str:
        return self.__str__()



################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 21/66: __init__.py
# Directorio: excepciones
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/excepciones/__init__.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 22/66: agua_agotada_exception.py
# Directorio: excepciones
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/excepciones/agua_agotada_exception.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 23/66: forestacion_exception.py
# Directorio: excepciones
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/excepciones/forestacion_exception.py
# ==============================================================================

class ForestacionException(Exception):
    """Excepción base para errores relacionados con forestación."""
    pass


# ==============================================================================
# ARCHIVO 24/66: mensaje_exception.py
# Directorio: excepciones
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/excepciones/mensaje_exception.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 25/66: persistencia_exception.py
# Directorio: excepciones
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/excepciones/persistencia_exception.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 26/66: superficie_insuficiente_exception.py
# Directorio: excepciones
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/excepciones/superficie_insuficiente_exception.py
# ==============================================================================

from .forestacion_exception import ForestacionException

class SuperficieInsuficienteException(ForestacionException):
    """Excepción lanzada cuando la superficie disponible es insuficiente."""
    pass



################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 27/66: __init__.py
# Directorio: patrones
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 28/66: __init__.py
# Directorio: patrones/factory
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/factory/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 29/66: cultivo_factory.py
# Directorio: patrones/factory
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/factory/cultivo_factory.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 30/66: __init__.py
# Directorio: patrones/observer
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/observer/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 31/66: observable.py
# Directorio: patrones/observer
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/observer/observable.py
# ==============================================================================

from typing import Generic, TypeVar, List
from abc import ABC
from python_forestacion.patrones.observer.observer import Observer

T = TypeVar('T')

class Observable(Generic[T], ABC):
    """Clase base para objetos observables (sujetos)."""
    
    def __init__(self) -> None:
        self._observadores: List[Observer[T]] = []
    
    def agregar_observador(self, observador: Observer[T]) -> None:
        """Agrega un observador a la lista si no estaba registrado."""
        if observador not in self._observadores:
            self._observadores.append(observador)
    
    def eliminar_observador(self, observador: Observer[T]) -> None:
        """Elimina un observador de la lista si estaba registrado."""
        if observador in self._observadores:
            self._observadores.remove(observador)
    
    def notificar_observadores(self, evento: T) -> None:
        """Notifica a todos los observadores registrados con el evento."""
        for observador in self._observadores:
            try:
                observador.actualizar(evento)
            except Exception as e:
                print(f"[Observable] Error notificando observador {observador}: {e}")
    
    def get_cantidad_observadores(self) -> int:
        """Devuelve la cantidad de observadores registrados."""
        return len(self._observadores)
    
    def limpiar_observadores(self) -> None:
        """Elimina todos los observadores registrados."""
        self._observadores.clear()


# ==============================================================================
# ARCHIVO 32/66: observer.py
# Directorio: patrones/observer
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/observer/observer.py
# ==============================================================================

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class Observer(Generic[T], ABC):
    """Interfaz para objetos observadores en el patrón Observer."""
    
    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """Método llamado cuando el observable notifica un cambio."""
        pass


################################################################################
# DIRECTORIO: patrones/observer/eventos
################################################################################

# ==============================================================================
# ARCHIVO 33/66: __init__.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/observer/eventos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 34/66: evento_plantacion.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/observer/eventos/evento_plantacion.py
# ==============================================================================

from dataclasses import dataclass
from datetime import datetime

@dataclass
class EventoPlantacion:
    """
    Representa un evento que ocurre en una plantación.
    """
    mensaje: str
    timestamp: datetime

# ==============================================================================
# ARCHIVO 35/66: evento_sensor.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/observer/eventos/evento_sensor.py
# ==============================================================================

from dataclasses import dataclass
from datetime import datetime

@dataclass
class EventoSensor:
    """
    Representa un evento de lectura de un sensor.
    """
    tipo_sensor: str
    valor: float
    timestamp: datetime


################################################################################
# DIRECTORIO: patrones/singleton
################################################################################

# ==============================================================================
# ARCHIVO 36/66: __init__.py
# Directorio: patrones/singleton
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/singleton/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 37/66: cultivo_service_registry.py
# Directorio: patrones/singleton
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/singleton/cultivo_service_registry.py
# ==============================================================================

from threading import Lock
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.olivo_service import OlivoService
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService

class CultivoServiceRegistry:
    """Singleton Registry para dispatch polimórfico de servicios de cultivos."""

    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._inicializar_servicios()
        return cls._instance

    @classmethod
    def get_instance(cls):
        """Obtiene la instancia singleton del registry."""
        if cls._instance is None:
            cls()
        return cls._instance

    def _inicializar_servicios(self):
        """Inicializa todos los servicios y registra los handlers."""
        # Inicializar servicios
        self._pino_service = PinoService()
        self._olivo_service = OlivoService()
        self._lechuga_service = LechugaService()
        self._zanahoria_service = ZanahoriaService()

        # Registrar handlers de absorción de agua
        self._absorber_agua_handlers = {
            Pino: self._pino_service.absorver_agua,
            Olivo: self._olivo_service.absorver_agua,
            Lechuga: self._lechuga_service.absorver_agua,
            Zanahoria: self._zanahoria_service.absorver_agua
        }

        # Registrar handlers de mostrar datos
        self._mostrar_datos_handlers = {
            Pino: self._pino_service.mostrar_datos,
            Olivo: self._olivo_service.mostrar_datos,
            Lechuga: self._lechuga_service.mostrar_datos,
            Zanahoria: self._zanahoria_service.mostrar_datos
        }

        # Registrar handlers de crecimiento
        self._hacer_crecer_handlers = {
            Pino: self._pino_service.hacer_crecer,
            Olivo: self._olivo_service.hacer_crecer
            # Lechuga y Zanahoria no crecen en altura
        }

    # Métodos públicos de dispatch polimórfico
    def absorber_agua(self, cultivo, fecha=None, temperatura=20.0, humedad=50.0):
        """Hace que un cultivo absorba agua."""
        tipo = type(cultivo)
        handler = self._absorber_agua_handlers.get(tipo)
        if handler is None:
            raise ValueError(f"Tipo de cultivo no soportado: {tipo}")
        return handler(cultivo, fecha, temperatura, humedad)

    def mostrar_datos(self, cultivo):
        """Muestra los datos de un cultivo."""
        tipo = type(cultivo)
        handler = self._mostrar_datos_handlers.get(tipo)
        if handler is None:
            raise ValueError(f"Tipo de cultivo no soportado: {tipo}")
        return handler(cultivo)

    def hacer_crecer(self, cultivo):
        """Hace crecer un cultivo en altura si corresponde."""
        tipo = type(cultivo)
        handler = self._hacer_crecer_handlers.get(tipo)
        if handler:
            return handler(cultivo)
        # Si no tiene handler, no hace nada
        return None



################################################################################
# DIRECTORIO: patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 38/66: __init__.py
# Directorio: patrones/strategy
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/strategy/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 39/66: absorcion_agua_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/strategy/absorcion_agua_strategy.py
# ==============================================================================

from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionAguaStrategy(ABC):
    """Interfaz Strategy para algoritmos de absorción de agua."""
    
    @abstractmethod
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        """
        Calcula la cantidad de agua que absorbe un cultivo.
        
        Args:
            fecha: Fecha actual para cálculos estacionales
            temperatura: Temperatura ambiental en °C
            humedad: Humedad ambiental en %
            cultivo: El cultivo que absorbe agua
            
        Returns:
            Cantidad de agua absorbida en litros
        """
        pass


################################################################################
# DIRECTORIO: patrones/strategy/impl
################################################################################

# ==============================================================================
# ARCHIVO 40/66: __init__.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/strategy/impl/__init__.py
# ==============================================================================


from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy

__all__ = [
    'AbsorcionSeasonalStrategy',
    'AbsorcionConstanteStrategy'
]

# ==============================================================================
# ARCHIVO 41/66: absorcion_constante_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
# ==============================================================================

from datetime import date
from typing import TYPE_CHECKING
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """Estrategia constante: siempre absorbe la misma cantidad."""
    
    def __init__(self, cantidad_constante: int):
        self._cantidad = cantidad_constante

    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        return self._cantidad  # Siempre la misma cantidad

# ==============================================================================
# ARCHIVO 42/66: absorcion_seasonal_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
# ==============================================================================

from datetime import date
from typing import TYPE_CHECKING
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.constantes import (
    MES_INICIO_VERANO, 
    MES_FIN_VERANO,
    ABSORCION_SEASONAL_VERANO,
    ABSORCION_SEASONAL_INVIERNO
)

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """Estrategia estacional: más agua en verano, menos en invierno."""
    
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        mes = fecha.month
        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO  # 5L en verano
        else:
            return ABSORCION_SEASONAL_INVIERNO  # 2L en invierno


################################################################################
# DIRECTORIO: riego
################################################################################

# ==============================================================================
# ARCHIVO 43/66: __init__.py
# Directorio: riego
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/riego/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: riego/control
################################################################################

# ==============================================================================
# ARCHIVO 44/66: __init__.py
# Directorio: riego/control
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/riego/control/__init__.py
# ==============================================================================

"""Controladores para el sistema de riego."""

from python_forestacion.riego.control.control_riego_task import ControlRiegoTask

__all__ = ['ControlRiegoTask']

# ==============================================================================
# ARCHIVO 45/66: control_riego_task.py
# Directorio: riego/control
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/riego/control/control_riego_task.py
# ==============================================================================

import threading
import time
from typing import Optional
from datetime import date
from python_forestacion.patrones.observer.observer import Observer
from python_forestacion.constantes import (
    INTERVALO_CONTROL_RIEGO,
    TEMP_MIN_RIEGO,
    TEMP_MAX_RIEGO,
    HUMEDAD_MAX_RIEGO
)

class ControlRiegoTask(threading.Thread, Observer[float]):
    """Controlador que observa sensores y riega automáticamente."""

    def __init__(self, sensor_temperatura, sensor_humedad, plantacion, plantacion_service):
        threading.Thread.__init__(self)
        Observer.__init__(self)

        self._sensor_temperatura = sensor_temperatura
        self._sensor_humedad = sensor_humedad
        self._plantacion = plantacion
        self._plantacion_service = plantacion_service

        self._detenido = threading.Event()
        self.daemon = True  # Thread daemon

        # Estado actual
        self._ultima_temperatura: Optional[float] = None
        self._ultima_humedad: Optional[float] = None
        self._riegos_realizados: int = 0

        # Registrar este controlador como observador de los sensores
        self._sensor_temperatura.agregar_observador(self)
        self._sensor_humedad.agregar_observador(self)

    def run(self) -> None:
        """Bucle principal del controlador de riego."""
        print("[ControlRiego] 🚀 Iniciando controlador de riego automático...")
        while not self._detenido.is_set():
            try:
                self._evaluar_condiciones_riego()
                self._detenido.wait(INTERVALO_CONTROL_RIEGO)  # Permite interrupción inmediata
            except Exception as e:
                print(f"[ControlRiego] ❌ Error en bucle de control: {e}")

    def actualizar(self, evento: float, sensor=None) -> None:
        """
        Método llamado por los sensores.
        Se pasa el sensor que envía el dato para distinguirlo.
        """
        if sensor == self._sensor_temperatura:
            self._ultima_temperatura = evento
            print(f"[ControlRiego] 🌡 Temperatura actualizada: {evento}°C")
        elif sensor == self._sensor_humedad:
            self._ultima_humedad = evento
            print(f"[ControlRiego] 💧 Humedad actualizada: {evento}%")
        else:
            print(f"[ControlRiego] ⚠️ Evento de sensor desconocido: {evento}")

    def _evaluar_condiciones_riego(self) -> None:
        """Evalúa las condiciones ambientales y decide si regar."""
        if self._ultima_temperatura is None or self._ultima_humedad is None:
            print("[ControlRiego] ⏳ Esperando datos de sensores...")
            return

        temp_ok = TEMP_MIN_RIEGO <= self._ultima_temperatura <= TEMP_MAX_RIEGO
        humedad_ok = self._ultima_humedad < HUMEDAD_MAX_RIEGO

        if temp_ok and humedad_ok:
            print(f"[ControlRiego] ✅ Condiciones óptimas (T:{self._ultima_temperatura}°C, H:{self._ultima_humedad}%)")
            self._realizar_riego_automatico()
        else:
            if not temp_ok:
                print(f"[ControlRiego] ❌ Temperatura fuera de rango (T:{self._ultima_temperatura}°C)")
            if not humedad_ok:
                print(f"[ControlRiego] ❌ Humedad muy alta (H:{self._ultima_humedad}%)")

    def _realizar_riego_automatico(self) -> None:
        """Realiza el riego automático de la plantación."""
        try:
            resumen = self._plantacion_service.regar(self._plantacion)
            self._riegos_realizados += 1

            print(f"[ControlRiego] 💦 Riego #{self._riegos_realizados} completado")
            print(f"[ControlRiego]   Agua consumida: {resumen['agua_consumida']}L")
            print(f"[ControlRiego]   Cultivos regados: {resumen['cultivos_regados']}")
            print(f"[ControlRiego]   Agua absorbida total: {resumen['agua_absorbida_total']}L")

            for tipo, datos in resumen["detalle_por_tipo"].items():
                print(f"[ControlRiego]   - {tipo}: {datos['cantidad']} cultivos, {datos['agua_absorbida']}L absorbida")
        except Exception as e:
            print(f"[ControlRiego] ❌ Error en riego automático: {e}")

    def detener(self) -> None:
        """Solicita la detención del hilo y desregistra los observadores."""
        self._detenido.set()
        print("[ControlRiego] 🛑 Deteniendo controlador de riego...")

        if hasattr(self._sensor_temperatura, "eliminar_observador"):
            self._sensor_temperatura.eliminar_observador(self)
        if hasattr(self._sensor_humedad, "eliminar_observador"):
            self._sensor_humedad.eliminar_observador(self)

    def get_estadisticas(self) -> dict:
        """Obtiene estadísticas del controlador."""
        return {
            "riegos_realizados": self._riegos_realizados,
            "ultima_temperatura": self._ultima_temperatura,
            "ultima_humedad": self._ultima_humedad,
            "condiciones_actuales": self._obtener_condiciones_actuales(),
            "observando_sensores": {
                "temperatura": id(self._sensor_temperatura),
                "humedad": id(self._sensor_humedad)
            }
        }

    def _obtener_condiciones_actuales(self) -> str:
        """Obtiene descripción de las condiciones actuales."""
        if self._ultima_temperatura is None or self._ultima_humedad is None:
            return "Esperando datos de sensores..."

        temp_ok = TEMP_MIN_RIEGO <= self._ultima_temperatura <= TEMP_MAX_RIEGO
        humedad_ok = self._ultima_humedad < HUMEDAD_MAX_RIEGO

        if temp_ok and humedad_ok:
            return f"Óptimas para riego (T:{self._ultima_temperatura}°C, H:{self._ultima_humedad}%)"
        elif not temp_ok:
            return f"Temperatura fuera de rango (T:{self._ultima_temperatura}°C, H:{self._ultima_humedad}%)"
        else:
            return f"Humedad muy alta (T:{self._ultima_temperatura}°C, H:{self._ultima_humedad}%)"

    def __str__(self) -> str:
        stats = self.get_estadisticas()
        return f"ControlRiegoTask(riegos={stats['riegos_realizados']}, estado={stats['condiciones_actuales']})"



################################################################################
# DIRECTORIO: riego/sensores
################################################################################

# ==============================================================================
# ARCHIVO 46/66: __init__.py
# Directorio: riego/sensores
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/riego/sensores/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 47/66: humedad_reader_task.py
# Directorio: riego/sensores
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/riego/sensores/humedad_reader_task.py
# ==============================================================================

import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_HUMEDAD,
    SENSOR_HUMEDAD_MIN,
    SENSOR_HUMEDAD_MAX
)

class HumedadReaderTask(threading.Thread, Observable[float]):
    """Sensor de humedad que notifica lecturas periódicamente."""
    
    def __init__(self):
        threading.Thread.__init__(self)
        Observable.__init__(self)
        self._detenido = threading.Event()
        self._contador_lecturas = 0
        self.daemon = True
        self.name = "HUM_" + str(id(self))

    def run(self) -> None:
        """Bucle principal del sensor de humedad."""
        print(f"[{self.name}] 💧 Sensor de humedad iniciado")
        
        while not self._detenido.is_set():
            try:
                # Simular lectura de humedad
                humedad = random.uniform(SENSOR_HUMEDAD_MIN, SENSOR_HUMEDAD_MAX)
                self._contador_lecturas += 1
                
                # Notificar a observadores
                self.notificar_observadores(humedad)
                
                # Debug
                if self._contador_lecturas % 100 == 0:
                    print(f"[{self.name}] 💧 Lectura #{self._contador_lecturas}: {humedad:.1f}%")
                
                time.sleep(INTERVALO_SENSOR_HUMEDAD)
                
            except Exception as e:
                print(f"[{self.name}] ❌ Error: {e}")
                time.sleep(INTERVALO_SENSOR_HUMEDAD)

    def detener(self) -> None:
        """Detiene el sensor de forma segura."""
        self._detenido.set()
        print(f"[{self.name}] 🛑 Sensor de humedad detenido")

    def get_contador_lecturas(self) -> int:
        """Retorna el número total de lecturas realizadas."""
        return self._contador_lecturas

# ==============================================================================
# ARCHIVO 48/66: temperatura_reader_task.py
# Directorio: riego/sensores
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/riego/sensores/temperatura_reader_task.py
# ==============================================================================

import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_TEMPERATURA,
    SENSOR_TEMP_MIN,
    SENSOR_TEMP_MAX
)

class TemperaturaReaderTask(threading.Thread, Observable[float]):
    """Sensor de temperatura que notifica lecturas periódicamente."""
    
    def __init__(self):
        threading.Thread.__init__(self)
        Observable.__init__(self)
        self._detenido = threading.Event()
        self._contador_lecturas = 0
        self.daemon = True
        self.name = "TEMP_" + str(id(self))

    def run(self) -> None:
        """Bucle principal del sensor de temperatura."""
        print(f"[{self.name}] 🔥 Sensor de temperatura iniciado")
        
        while not self._detenido.is_set():
            try:
                # Simular lectura de temperatura
                temperatura = random.uniform(SENSOR_TEMP_MIN, SENSOR_TEMP_MAX)
                self._contador_lecturas += 1
                
                # Notificar a observadores
                self.notificar_observadores(temperatura)
                
                # Debug
                if self._contador_lecturas % 100 == 0:
                    print(f"[{self.name}] 📊 Lectura #{self._contador_lecturas}: {temperatura:.1f}°C")
                
                time.sleep(INTERVALO_SENSOR_TEMPERATURA)
                
            except Exception as e:
                print(f"[{self.name}] ❌ Error: {e}")
                time.sleep(INTERVALO_SENSOR_TEMPERATURA)

    def detener(self) -> None:
        """Detiene el sensor de forma segura."""
        self._detenido.set()
        print(f"[{self.name}] 🛑 Sensor de temperatura detenido")

    def get_contador_lecturas(self) -> int:
        """Retorna el número total de lecturas realizadas."""
        return self._contador_lecturas


################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 49/66: __init__.py
# Directorio: servicios
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: servicios/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 50/66: __init__.py
# Directorio: servicios/cultivos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/cultivos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 51/66: arbol_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/cultivos/arbol_service.py
# ==============================================================================

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class ArbolService(CultivoService):
    """Servicio base genérico para arboles como Pino y Olivo."""
    
    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        super().__init__(estrategia_absorcion)
    
    def _imprimir_datos_arbol(self, cultivo) -> None:
        """Imprime los datos comunes y específicos de un árbol."""
        self._mostrar_datos_base(cultivo)
        print(f"Identificador: {cultivo.get_id()}")
        print(f"Altura actual: {cultivo.get_altura()} m")


# ==============================================================================
# ARCHIVO 52/66: cultivo_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/cultivos/cultivo_service.py
# ==============================================================================

from abc import ABC, abstractmethod
from datetime import date
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class CultivoService(ABC):
    """Servicio base para todos los cultivos."""
    
    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        self._estrategia_absorcion = estrategia_absorcion

    def absorver_agua(self, cultivo: Cultivo, fecha: date, temperatura: float, humedad: float) -> int:
        """
        El cultivo absorbe agua según su estrategia.
        
        Returns:
            Cantidad de agua absorbida en litros
        """
        agua_absorvida = self._estrategia_absorcion.calcular_absorcion(
            fecha, temperatura, humedad, cultivo
        )
        
        # Actualizar agua del cultivo
        cultivo.set_agua(cultivo.get_agua() + agua_absorvida)
        
        return agua_absorvida

    @abstractmethod
    def mostrar_datos(self, cultivo: Cultivo) -> None:
        """Muestra los datos específicos del cultivo."""
        pass

    @abstractmethod
    def hacer_crecer(self, cultivo: Cultivo) -> None:
        """Hace crecer al cultivo (implementación específica por tipo)."""
        pass

# ==============================================================================
# ARCHIVO 53/66: cultivo_service_registry.py
# Directorio: servicios/cultivos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ==============================================================================

from threading import Lock
from typing import Dict, Type, Callable
from datetime import date

from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

class CultivoServiceRegistry:
    """
    Registry singleton para servicios de cultivos.
    Maneja dispatch polimórfico evitando instanceof.
    """
    
    _instance = None
    _lock = Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._init_servicios()
        return cls._instance
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance
    
    def _init_servicios(self):
        """Inicializa todos los servicios y los handlers."""
        from python_forestacion.servicios.cultivos.pino_service import PinoService
        from python_forestacion.servicios.cultivos.olivo_service import OlivoService
        from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
        from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService
        
        self._pino_srv = PinoService()
        self._olivo_srv = OlivoService()
        self._lechuga_srv = LechugaService()
        self._zanahoria_srv = ZanahoriaService()
        
        self._absorber_agua_handlers: Dict[Type[Cultivo], Callable] = {
            Pino: self._absorber_pino,
            Olivo: self._absorber_olivo,
            Lechuga: self._absorber_lechuga,
            Zanahoria: self._absorber_zanahoria
        }
        
        self._mostrar_datos_handlers: Dict[Type[Cultivo], Callable] = {
            Pino: self._mostrar_pino,
            Olivo: self._mostrar_olivo,
            Lechuga: self._mostrar_lechuga,
            Zanahoria: self._mostrar_zanahoria
        }
        
        self._hacer_crecer_handlers: Dict[Type[Cultivo], Callable] = {
            Pino: self._hacer_crecer_pino,
            Olivo: self._hacer_crecer_olivo
        }
    
    # === MÉTODOS PÚBLICOS ===
    
    def absorber_agua(self, cultivo: Cultivo, fecha: date = None, temp: float = 20.0, hum: float = 50.0) -> int:
        tipo = type(cultivo)
        if tipo not in self._absorber_agua_handlers:
            raise ValueError(f"Cultivo no registrado: {tipo}")
        return self._absorber_agua_handlers[tipo](cultivo, fecha, temp, hum)
    
    def mostrar_datos(self, cultivo: Cultivo) -> None:
        tipo = type(cultivo)
        if tipo not in self._mostrar_datos_handlers:
            raise ValueError(f"Cultivo no registrado: {tipo}")
        self._mostrar_datos_handlers[tipo](cultivo)
    
    def hacer_crecer(self, cultivo: Cultivo) -> None:
        tipo = type(cultivo)
        if tipo in self._hacer_crecer_handlers:
            self._hacer_crecer_handlers[tipo](cultivo)
    
    # === HANDLERS ===
    
    def _absorber_pino(self, cultivo: Pino, fecha: date, temp: float, hum: float) -> int:
        return self._pino_srv.absorver_agua(cultivo, fecha, temp, hum)
    
    def _mostrar_pino(self, cultivo: Pino) -> None:
        self._pino_srv.mostrar_datos(cultivo)
    
    def _hacer_crecer_pino(self, cultivo: Pino) -> None:
        self._pino_srv.hacer_crecer(cultivo)
    
    def _absorber_olivo(self, cultivo: Olivo, fecha: date, temp: float, hum: float) -> int:
        return self._olivo_srv.absorver_agua(cultivo, fecha, temp, hum)
    
    def _mostrar_olivo(self, cultivo: Olivo) -> None:
        self._olivo_srv.mostrar_datos(cultivo)
    
    def _hacer_crecer_olivo(self, cultivo: Olivo) -> None:
        self._olivo_srv.hacer_crecer(cultivo)
    
    def _absorber_lechuga(self, cultivo: Lechuga, fecha: date, temp: float, hum: float) -> int:
        return self._lechuga_srv.absorver_agua(cultivo, fecha, temp, hum)
    
    def _mostrar_lechuga(self, cultivo: Lechuga) -> None:
        self._lechuga_srv.mostrar_datos(cultivo)
    
    def _absorber_zanahoria(self, cultivo: Zanahoria, fecha: date, temp: float, hum: float) -> int:
        return self._zanahoria_srv.absorver_agua(cultivo, fecha, temp, hum)
    
    def _mostrar_zanahoria(self, cultivo: Zanahoria) -> None:
        self._zanahoria_srv.mostrar_datos(cultivo)
    
    # === MÉTODOS DE VERIFICACIÓN ===
    
    def verificar_singleton(self) -> bool:
        inst1 = CultivoServiceRegistry()
        inst2 = CultivoServiceRegistry()
        inst3 = CultivoServiceRegistry.get_instance()
        return inst1 is inst2 is inst3
    
    def get_cantidad_handlers(self) -> dict:
        return {
            "absorber_agua": len(self._absorber_agua_handlers),
            "mostrar_datos": len(self._mostrar_datos_handlers),
            "hacer_crecer": len(self._hacer_crecer_handlers),
            "tipos": list(self._absorber_agua_handlers.keys())
        }
    
    def __str__(self):
        return f"CultivoServiceRegistry({self.get_cantidad_handlers()})"
    
    __repr__ = __str__


# ==============================================================================
# ARCHIVO 54/66: lechuga_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/cultivos/lechuga_service.py
# ==============================================================================

from datetime import date
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_CONSTANTE_LECHUGA

class LechugaService(CultivoService):
    """Servicio específico para cultivos de tipo Lechuga."""
    
    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_CONSTANTE_LECHUGA))
    
    def absorver_agua(self, cultivo: Lechuga, fecha: date, temperatura: float, humedad: float) -> int:
        """La lechuga absorbe agua constante."""
        return super().absorver_agua(cultivo, fecha, temperatura, humedad)
    
    def hacer_crecer(self, cultivo: Lechuga) -> None:
        """Las lechugas no crecen en altura."""
        pass  # Las hortalizas no crecen en altura
    
    def mostrar_datos(self, cultivo: Lechuga) -> None:
        """Muestra los datos específicos de la lechuga."""
        print(f"Cultivo: Lechuga")
        print(f"Superficie: {cultivo.get_superficie()} m²")
        print(f"Agua almacenada: {cultivo.get_agua()} L")
        print(f"Variedad: {cultivo.get_variedad()}")
        print(f"Invernadero: {'Sí' if cultivo.get_invernadero() else 'No'}")
        print("-" * 20)

# ==============================================================================
# ARCHIVO 55/66: olivo_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/cultivos/olivo_service.py
# ==============================================================================

from datetime import date
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_OLIVO

class OlivoService(ArbolService):
    """Servicio específico para cultivos de tipo Olivo."""
    
    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())
    
    def absorver_agua(self, cultivo: Olivo, fecha: date, temperatura: float, humedad: float) -> int:
        """El olivo absorbe agua según estrategia estacional."""
        return super().absorver_agua(cultivo, fecha, temperatura, humedad)
    
    def hacer_crecer(self, cultivo: Olivo) -> None:
        """El olivo crece en altura cuando se riega."""
        cultivo.crecer(CRECIMIENTO_OLIVO)
        print(f"Olivo {cultivo.get_id()} creció a {cultivo.get_altura():.2f}m")
    
    def mostrar_datos(self, cultivo: Olivo) -> None:
        """Muestra los datos específicos del olivo."""
        print(f"Cultivo: Olivo")
        print(f"Superficie: {cultivo.get_superficie()} m²")
        print(f"Agua almacenada: {cultivo.get_agua()} L")
        print(f"ID: {cultivo.get_id()}")
        print(f"Altura: {cultivo.get_altura():.2f} m")
        print(f"Variedad: {cultivo.get_variedad()}")
        print("-" * 20)

# ==============================================================================
# ARCHIVO 56/66: pino_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/cultivos/pino_service.py
# ==============================================================================

from datetime import date
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_PINO

class PinoService(ArbolService):
    """Servicio específico para cultivos de tipo Pino."""
    
    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())
    
    def absorver_agua(self, cultivo: Pino, fecha: date, temperatura: float, humedad: float) -> int:
        """El pino absorbe agua según estrategia estacional."""
        return super().absorver_agua(cultivo, fecha, temperatura, humedad)
    
    def hacer_crecer(self, cultivo: Pino) -> None:
        """El pino crece en altura cuando se riega."""
        cultivo.crecer(CRECIMIENTO_PINO)
        print(f"Pino {cultivo.get_id()} creció a {cultivo.get_altura():.2f}m")
    
    def mostrar_datos(self, cultivo: Pino) -> None:
        """Muestra los datos específicos del pino."""
        print(f"Cultivo: Pino")
        print(f"Superficie: {cultivo.get_superficie()} m²")
        print(f"Agua almacenada: {cultivo.get_agua()} L")
        print(f"ID: {cultivo.get_id()}")
        print(f"Altura: {cultivo.get_altura():.2f} m")
        print(f"Variedad: {cultivo.get_variedad()}")
        print("-" * 20)

# ==============================================================================
# ARCHIVO 57/66: zanahoria_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/cultivos/zanahoria_service.py
# ==============================================================================

from datetime import date
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_CONSTANTE_ZANAHORIA

class ZanahoriaService(CultivoService):
    """Servicio específico para cultivos de tipo Zanahoria."""
    
    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_CONSTANTE_ZANAHORIA))
    
    def absorver_agua(self, cultivo: Zanahoria, fecha: date, temperatura: float, humedad: float) -> int:
        """La zanahoria absorbe agua constante."""
        return super().absorver_agua(cultivo, fecha, temperatura, humedad)
    
    def hacer_crecer(self, cultivo: Zanahoria) -> None:
        """Las zanahorias no crecen en altura."""
        pass  # Las hortalizas no crecen en altura
    
    def mostrar_datos(self, cultivo: Zanahoria) -> None:
        """Muestra los datos específicos de la zanahoria."""
        print(f"Cultivo: Zanahoria")
        print(f"Superficie: {cultivo.get_superficie()} m²")
        print(f"Agua almacenada: {cultivo.get_agua()} L")
        print(f"Variedad: {cultivo.get_variedad()}")
        print(f"Invernadero: {'Sí' if cultivo.get_invernadero() else 'No'}")
        print(f"Baby Carrot: {'Sí' if cultivo.is_baby_carrot() else 'No'}")
        print("-" * 20)


################################################################################
# DIRECTORIO: servicios/negocio
################################################################################

# ==============================================================================
# ARCHIVO 58/66: __init__.py
# Directorio: servicios/negocio
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/negocio/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 59/66: fincas_service.py
# Directorio: servicios/negocio
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/negocio/fincas_service.py
# ==============================================================================

from typing import Dict, Type, List
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.servicios.negocio.paquete import Paquete

class FincasService:
    """Servicio de alto nivel para gestionar múltiples fincas."""
    
    def __init__(self):
        self._fincas: Dict[int, RegistroForestal] = {}  # id_padron -> RegistroForestal

    def add_finca(self, registro: RegistroForestal) -> None:
        """Agrega una finca al sistema."""
        id_padron = registro.get_id_padron()
        self._fincas[id_padron] = registro
        print(f"🏠 Finca agregada: Padron {id_padron}, Propietario: {registro.get_propietario()}")

    def buscar_finca(self, id_padron: int) -> RegistroForestal:
        """Busca una finca por ID de padrón."""
        if id_padron not in self._fincas:
            raise ValueError(f"Finca con padrón {id_padron} no encontrada")
        return self._fincas[id_padron]

    def fumigar(self, id_padron: int, plaguicida: str) -> None:
        """Fumiga toda la plantación de una finca."""
        registro = self.buscar_finca(id_padron)
        plantacion = registro.get_plantacion()
        print(f"🦠 Fumigando plantación '{plantacion.get_nombre()}' con: {plaguicida}")
        # En una implementación real, aquí se aplicaría el plaguicida a todos los cultivos

    def cosechar_y_empaquetar(self, tipo_cultivo: Type[Cultivo]) -> Paquete:
        """Cosecha todos los cultivos de un tipo específico y los empaqueta."""
        cultivos_cosechados = []
        
        for registro in self._fincas.values():
            plantacion = registro.get_plantacion()
            cultivos_plantacion = plantacion.get_cultivos()
            
            # Filtrar cultivos del tipo especificado
            cultivos_tipo = [c for c in cultivos_plantacion if isinstance(c, tipo_cultivo)]
            cultivos_cosechados.extend(cultivos_tipo)
            
            # Remover de la plantación
            for cultivo in cultivos_tipo:
                plantacion.remover_cultivo(cultivo)
        
        # Crear paquete
        paquete = Paquete(tipo_cultivo, cultivos_cosechados)
        print(f"📦 Cosechados {len(cultivos_cosechados)} {tipo_cultivo.__name__}(s)")
        
        return paquete

    def get_cantidad_fincas(self) -> int:
        """Retorna la cantidad de fincas registradas."""
        return len(self._fincas)

    def listar_fincas(self) -> List[Dict]:
        """Retorna información resumida de todas las fincas."""
        return [
            {
                'padron': registro.get_id_padron(),
                'propietario': registro.get_propietario(),
                'avaluo': registro.get_avaluo(),
                'cultivos': len(registro.get_plantacion().get_cultivos())
            }
            for registro in self._fincas.values()
        ]

# ==============================================================================
# ARCHIVO 60/66: paquete.py
# Directorio: servicios/negocio
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/negocio/paquete.py
# ==============================================================================

from typing import List, TypeVar, Generic, Type
from python_forestacion.entidades.cultivos.cultivo import Cultivo

T = TypeVar('T', bound=Cultivo)

class Paquete(Generic[T]):
    """Paquete genérico tipo-seguro para empaquetar cultivos cosechados."""
    
    _contador_id = 0

    def __init__(self, tipo_cultivo: Type[T], cultivos: List[T]):
        Paquete._contador_id += 1
        self._id_paquete = Paquete._contador_id
        self._tipo_cultivo = tipo_cultivo
        self._cultivos = cultivos

    def get_id_paquete(self) -> int:
        return self._id_paquete

    def get_tipo_cultivo(self) -> Type[T]:
        return self._tipo_cultivo

    def get_cultivos(self) -> List[T]:
        return self._cultivos.copy()

    def get_cantidad(self) -> int:
        return len(self._cultivos)

    def mostrar_contenido_caja(self) -> None:
        """Muestra el contenido del paquete."""
        print(f"\n📦 Contenido de la caja #{self._id_paquete}:")
        print(f"  Tipo: {self._tipo_cultivo.__name__}")
        print(f"  Cantidad: {self.get_cantidad()}")
        print(f"  IDs de cultivos: {[c.get_id() for c in self._cultivos]}")

    def __str__(self) -> str:
        return f"Paquete(id={self._id_paquete}, tipo={self._tipo_cultivo.__name__}, cantidad={self.get_cantidad()})"

    def __repr__(self) -> str:
        return f"Paquete(id_paquete={self._id_paquete}, tipo_cultivo={self._tipo_cultivo}, cultivos={self._cultivos})"


################################################################################
# DIRECTORIO: servicios/personal
################################################################################

# ==============================================================================
# ARCHIVO 61/66: __init__.py
# Directorio: servicios/personal
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/personal/__init__.py
# ==============================================================================

"""Servicios relacionados con la gestión de personal y tareas de campo."""

from python_forestacion.servicios.personal.trabajador_service import TrabajadorService

__all__ = ["TrabajadorService"]


# ==============================================================================
# ARCHIVO 62/66: trabajador_service.py
# Directorio: servicios/personal
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/personal/trabajador_service.py
# ==============================================================================

from datetime import date
from typing import List
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.apto_medico import AptoMedico
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.herramienta import Herramienta

class TrabajadorService:
    """
    Servicio para operaciones relacionadas con los trabajadores.
    Permite crear, asignar aptos médicos, ejecutar tareas y verificar estados.
    """

    def __init__(self):
        """Inicializa el servicio de gestión de trabajadores."""
        pass

    def crear_trabajador(self, dni: int, nombre: str, tareas: List[Tarea] = None) -> Trabajador:
        """
        Crea un nuevo trabajador validando los datos de entrada.
        """
        self._validar_datos_trabajador(dni, nombre)

        trabajador = Trabajador(
            dni=dni,
            nombre=nombre,
            tareas=tareas if tareas is not None else []
        )

        print(f"👷 Trabajador creado: {trabajador.get_nombre()} (DNI: {trabajador.get_dni()})")
        return trabajador

    def _validar_datos_trabajador(self, dni: int, nombre: str) -> None:
        """Valida los datos de entrada al crear un trabajador."""
        if not isinstance(dni, int):
            raise ValueError("El DNI debe ser un número entero")
        if dni <= 0:
            raise ValueError("El DNI debe ser un número positivo")
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

    def asignar_apto_medico(self, trabajador: Trabajador, apto: bool, fecha_emision: date, observaciones: str = None) -> AptoMedico:
        """
        Asigna un apto médico a un trabajador.
        """
        apto_medico = AptoMedico(
            apto=apto,
            fecha_emision=fecha_emision,
            observaciones=observaciones
        )

        trabajador.set_apto_medico(apto_medico)
        print(f"🩺 Apto médico asignado a {trabajador.get_nombre()} ({'Apto' if apto else 'No apto'})")
        return apto_medico

    @staticmethod
    def _obtener_id_tarea(tarea: Tarea) -> int:
        """Método auxiliar para obtener el ID de una tarea."""
        return tarea.get_id()

    def trabajar(self, trabajador: Trabajador, fecha: date, herramienta: Herramienta) -> bool:
        """
        Ejecuta las tareas asignadas a un trabajador.
        """
        if not trabajador.tiene_apto_medico_valido():
            print(f"  {trabajador.get_nombre()} no puede trabajar: sin apto médico válido.")
            return False

        tareas_del_dia = [
            t for t in trabajador.get_tareas()
            if t.get_fecha_programada() == fecha and t.esta_pendiente()
        ]

        if not tareas_del_dia:
            print(f"  {trabajador.get_nombre()} no tiene tareas pendientes para {fecha}.")
            return True

        # Ordenar tareas por ID descendente (US-016)
        tareas_ordenadas = sorted(
            tareas_del_dia,
            key=self._obtener_id_tarea,
            reverse=True
        )

        print(f" {trabajador.get_nombre()} trabajando con {herramienta.get_nombre()}...")

        for tarea in tareas_ordenadas:
            print(f" Realizando tarea {tarea.get_id()}: {tarea.get_descripcion()}")
            tarea.completar()

        print(f"   {len(tareas_ordenadas)} tareas completadas con éxito.")
        return True

    def verificar_estado_trabajador(self, trabajador: Trabajador) -> dict:
        """
        Retorna un resumen del estado del trabajador.
        """
        tareas = trabajador.get_tareas()
        tareas_pendientes = [t for t in tareas if t.esta_pendiente()]
        tareas_completadas = [t for t in tareas if not t.esta_pendiente()]

        return {
            "dni": trabajador.get_dni(),
            "nombre": trabajador.get_nombre(),
            "tiene_apto": trabajador.tiene_apto_medico_valido(),
            "apto_medico": trabajador.get_apto_medico(),
            "total_tareas": len(tareas),
            "tareas_pendientes": len(tareas_pendientes),
            "tareas_completadas": len(tareas_completadas)
        }


################################################################################
# DIRECTORIO: servicios/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 63/66: __init__.py
# Directorio: servicios/terrenos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/terrenos/__init__.py
# ==============================================================================

"""Servicios de dominio relacionados con terrenos, tierras, plantaciones y registros forestales."""

from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService

__all__ = [
    "TierraService",
    "PlantacionService",
    "RegistroForestalService"
]


# ==============================================================================
# ARCHIVO 64/66: plantacion_service.py
# Directorio: servicios/terrenos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/terrenos/plantacion_service.py
# ==============================================================================

from typing import List, Dict
from datetime import date
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.constantes import AGUA_MINIMA

class PlantacionService:
    
    def plantar(self, plantacion: Plantacion, especie: str, cantidad: int) -> List:
        """
        Planta múltiples cultivos de una especie en la plantación.
        
        Args:
            plantacion: La plantación donde plantar
            especie: Tipo de cultivo ("Pino", "Olivo", "Lechuga", "Zanahoria")
            cantidad: Número de cultivos a plantar
            
        Returns:
            Lista de cultivos plantados
            
        Raises:
            SuperficieInsuficienteException: Si no hay suficiente superficie
        """
        # Calcular superficie requerida
        cultivo_ejemplo = CultivoFactory.crear_cultivo(especie)
        superficie_requerida = cultivo_ejemplo.get_superficie() * cantidad
        
        # Verificar superficie disponible
        superficie_disponible = self._calcular_superficie_disponible(plantacion)
        
        if superficie_requerida > superficie_disponible:
            raise SuperficieInsuficienteException(
                f"No hay suficiente superficie para plantar {cantidad} {especie}(s)",
                f"Superficie requerida: {superficie_requerida}, disponible: {superficie_disponible}",
                superficie_requerida,
                superficie_disponible
            )
        
        # Crear y agregar cultivos
        cultivos_creados = []
        for _ in range(cantidad):
            cultivo = CultivoFactory.crear_cultivo(especie)
            plantacion.agregar_cultivo(cultivo)
            cultivos_creados.append(cultivo)
        
        return cultivos_creados
    
    def _calcular_superficie_disponible(self, plantacion: Plantacion) -> float:
        """Calcula la superficie disponible en la plantación."""
        superficie_ocupada = sum(
            cultivo.get_superficie() for cultivo in plantacion.get_cultivos()
        )
        return plantacion.get_superficie() - superficie_ocupada
    
    def regar(self, plantacion: Plantacion) -> Dict:
        """
        Riega todos los cultivos de la plantación.
        
        Returns:
            Dict con resumen del riego:
            {
                'agua_consumida': int,
                'cultivos_regados': int,
                'agua_absorbida_total': int,
                'detalle_por_tipo': dict,
                'agua_restante': float
            }
        """
        # Verificar agua disponible
        agua_disponible = plantacion.get_agua()
        if agua_disponible < AGUA_MINIMA:
            raise AguaAgotadaException(
                "No hay suficiente agua para regar la plantación",
                f"Agua disponible: {agua_disponible}, mínima requerida: {AGUA_MINIMA}",
                agua_disponible,
                AGUA_MINIMA
            )
        
        # Obtener registry
        registry = CultivoServiceRegistry.get_instance()
        
        # Variables para el resumen
        agua_consumida_total = 0
        cultivos_regados = 0
        agua_absorbida_total = 0
        detalle_por_tipo = {}
        
        # Obtener condiciones ambientales (simuladas)
        fecha_actual = date.today()
        temperatura = 20.0  # °C simulada
        humedad = 60.0      # % simulada
        
        # Regar cada cultivo
        for cultivo in plantacion.get_cultivos():
            try:
                # Usar registry para absorber agua
                agua_absorbida = registry.absorber_agua(cultivo, fecha_actual, temperatura, humedad)
                
                # Actualizar estadísticas
                agua_absorbida_total += agua_absorbida
                cultivos_regados += 1
                
                # Actualizar detalle por tipo
                tipo_cultivo = type(cultivo).__name__
                if tipo_cultivo not in detalle_por_tipo:
                    detalle_por_tipo[tipo_cultivo] = {
                        'cantidad': 0,
                        'agua_absorbida': 0
                    }
                detalle_por_tipo[tipo_cultivo]['cantidad'] += 1
                detalle_por_tipo[tipo_cultivo]['agua_absorbida'] += agua_absorbida
                
                # Hacer crecer los árboles (solo pinos y olivos)
                registry.hacer_crecer(cultivo)
                
            except Exception as e:
                print(f"Error regando cultivo {cultivo.get_id()}: {e}")
                continue
        
        # Consumir agua de la plantación
        agua_consumida_total = agua_absorbida_total
        plantacion.descontar_agua(agua_consumida_total)
        
        # Retornar resumen
        return {
            'agua_consumida': agua_consumida_total,
            'cultivos_regados': cultivos_regados,
            'agua_absorbida_total': agua_absorbida_total,
            'detalle_por_tipo': detalle_por_tipo,
            'agua_restante': plantacion.get_agua()
        }
    
    def get_estado_plantacion(self, plantacion: Plantacion) -> dict:
        """Obtiene el estado actual de la plantación."""
        cultivos = plantacion.get_cultivos()
        superficie_ocupada = sum(cultivo.get_superficie() for cultivo in cultivos)
        superficie_disponible = plantacion.get_superficie() - superficie_ocupada
        
        return {
            'cantidad_cultivos': len(cultivos),
            'superficie_ocupada': superficie_ocupada,
            'superficie_disponible': superficie_disponible,
            'agua_disponible': plantacion.get_agua()
        }

# ==============================================================================
# ARCHIVO 65/66: registro_forestal_service.py
# Directorio: servicios/terrenos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/terrenos/registro_forestal_service.py
# ==============================================================================

import os
import pickle
from typing import TYPE_CHECKING

# Importaciones directas para ejecución normal
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.persistencia_exception import PersistenciaException
from python_forestacion.constantes import DIRECTORIO_DATA, EXTENSION_DATA

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal


class RegistroForestalService:
    """Servicio encargado de la gestión, validación y persistencia de registros forestales."""

    def __init__(self) -> None:
        # Podríamos agregar un logger en el futuro
        pass

    # ======================================================
    # CREACIÓN
    # ======================================================
    def crear_registro_forestal(
        self,
        id_padron: int,
        tierra: Tierra,
        plantacion: Plantacion,
        propietario: str,
        avaluo: float
    ) -> RegistroForestal:
        """
        Crea un registro forestal completo aplicando validaciones básicas.
        """
        self._validar_datos_registro(id_padron, tierra, plantacion, propietario, avaluo)

        registro = RegistroForestal(
            id_padron=id_padron,
            tierra=tierra,
            plantacion=plantacion,
            propietario=propietario,
            avaluo=avaluo
        )

        print(f"\n📋 Registro forestal creado correctamente para {propietario}")
        print(f"   → ID Padrón: {id_padron}")
        print(f"   → Avaluo: {avaluo:,.2f}")
        print(f"   → Domicilio: {tierra.get_domicilio()}")
        return registro

    # ======================================================
    # VALIDACIÓN
    # ======================================================
    def _validar_datos_registro(
        self,
        id_padron: int,
        tierra: Tierra,
        plantacion: Plantacion,
        propietario: str,
        avaluo: float
    ) -> None:
        """Valida los datos necesarios antes de crear un registro forestal."""

        if not isinstance(id_padron, int) or id_padron <= 0:
            raise ValueError("El ID de padrón debe ser un número entero positivo.")

        if not isinstance(tierra, Tierra):
            raise ValueError("Debe proporcionarse una instancia válida de Tierra.")

        if not isinstance(plantacion, Plantacion):
            raise ValueError("Debe proporcionarse una instancia válida de Plantacion.")

        if not isinstance(propietario, str) or not propietario.strip():
            raise ValueError("El nombre del propietario no puede estar vacío.")

        if not isinstance(avaluo, (int, float)) or avaluo <= 0:
            raise ValueError("El avalúo debe ser un número positivo.")

    # ======================================================
    # VISUALIZACIÓN
    # ======================================================
    def mostrar_datos(self, registro: RegistroForestal) -> None:
        """Muestra los datos del registro forestal con formato legible."""
        print("\n🌳 REGISTRO FORESTAL")
        print("=====================")
        print(f"📄 ID Padrón:       {registro.get_id_padron()}")
        print(f"👤 Propietario:     {registro.get_propietario()}")
        print(f"💰 Avalúo Fiscal:   {registro.get_avaluo():,.2f}")
        print(f"🏠 Domicilio:       {registro.get_tierra().get_domicilio()}")
        print(f"📏 Superficie:      {registro.get_tierra().get_superficie()} m²")

        cultivos = registro.get_plantacion().get_cultivos()
        cantidad_cultivos = len(cultivos)
        print(f"🌾 Cantidad de cultivos: {cantidad_cultivos}")

        if cantidad_cultivos > 0:
            print("🧺 Ejemplo de cultivos:")
            for c in cultivos[:3]:
                print(f"   → {c}")
            if cantidad_cultivos > 3:
                print(f"   ... y {cantidad_cultivos - 3} más.")

    # ======================================================
    # PERSISTENCIA
    # ======================================================
    def persistir(self, registro: RegistroForestal) -> None:
        """Guarda el registro forestal en disco utilizando Pickle."""
        try:
            if not os.path.exists(DIRECTORIO_DATA):
                os.makedirs(DIRECTORIO_DATA)

            nombre_archivo = f"{registro.get_propietario()}{EXTENSION_DATA}"
            ruta_archivo = os.path.join(DIRECTORIO_DATA, nombre_archivo)

            with open(ruta_archivo, "wb") as archivo:
                pickle.dump(registro, archivo)

            print(f"\n💾 Registro de {registro.get_propietario()} guardado exitosamente en {ruta_archivo}")

        except Exception as e:
            raise PersistenciaException(
                user_message=f"Error al guardar registro de {registro.get_propietario()}",
                technical_message=str(e),
                nombre_archivo=nombre_archivo,
                tipo_operacion="ESCRITURA"
            )

    # ======================================================
    # LECTURA
    # ======================================================
    @staticmethod
    def leer_registro(propietario: str) -> RegistroForestal:
        """Recupera un registro forestal previamente persistido en disco."""
        if not propietario or not propietario.strip():
            raise ValueError("El nombre del propietario no puede ser nulo o vacío.")

        try:
            nombre_archivo = f"{propietario}{EXTENSION_DATA}"
            ruta_archivo = os.path.join(DIRECTORIO_DATA, nombre_archivo)

            if not os.path.exists(ruta_archivo):
                raise PersistenciaException(
                    user_message=f"No se encontró registro de {propietario}.",
                    technical_message=f"Archivo no existe: {ruta_archivo}",
                    nombre_archivo=nombre_archivo,
                    tipo_operacion="LECTURA"
                )

            with open(ruta_archivo, "rb") as archivo:
                registro = pickle.load(archivo)

            print(f"\n📂 Registro de {propietario} leído correctamente desde {ruta_archivo}")
            return registro

        except PersistenciaException:
            raise
        except Exception as e:
            raise PersistenciaException(
                user_message=f"Error al leer registro de {propietario}",
                technical_message=str(e),
                nombre_archivo=nombre_archivo,
                tipo_operacion="LECTURA"
            )


# ==============================================================================
# ARCHIVO 66/66: tierra_service.py
# Directorio: servicios/terrenos
# Ruta completa: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/terrenos/tierra_service.py
# ==============================================================================

from typing import TYPE_CHECKING

# Importaciones directas
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.constantes import (
    PADRON_CATASTRAL_MINIMO,
    SUPERFICIE_MINIMA,
    AGUA_INICIAL_PLANTACION
)

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.tierra import Tierra
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class TierraService:
    """Servicio para la creación, modificación y gestión de Tierras."""

    def __init__(self):
        pass

    # ======================================================
    # CREACIÓN DE TIERRA
    # ======================================================
    def crear_tierra(self, id_padron_catastral: int, superficie: float, domicilio: str) -> Tierra:
        """Crea una nueva tierra con validación de datos."""
        self._validar_datos_tierra(id_padron_catastral, superficie, domicilio)

        tierra = Tierra(
            id_padron_catastral=id_padron_catastral,
            superficie=superficie,
            domicilio=domicilio
        )

        print(f"\n🏡 Tierra creada con éxito (Padron: {id_padron_catastral})")
        print(f"   → Superficie: {superficie} m²")
        print(f"   → Domicilio: {domicilio}")
        return tierra

    def crear_tierra_con_plantacion(
        self,
        id_padron_catastral: int,
        superficie: float,
        domicilio: str,
        nombre_plantacion: str
    ) -> Tierra:
        """
        Crea una tierra con su plantación asociada.
        """
        tierra = self.crear_tierra(id_padron_catastral, superficie, domicilio)

        plantacion = Plantacion(
            nombre=nombre_plantacion,
            superficie=superficie,
            agua=AGUA_INICIAL_PLANTACION
        )

        tierra.set_finca(plantacion)

        print(f"🌱 Plantación '{nombre_plantacion}' asociada a la tierra (Padron: {id_padron_catastral})")
        return tierra

    # ======================================================
    # VALIDACIÓN DE DATOS
    # ======================================================
    def _validar_datos_tierra(self, id_padron_catastral: int, superficie: float, domicilio: str) -> None:
        """Valida los datos de entrada para crear o modificar una tierra."""
        # Padron catastral
        if not isinstance(id_padron_catastral, int):
            raise ValueError("El padron catastral debe ser un número entero.")
        if id_padron_catastral < PADRON_CATASTRAL_MINIMO:
            raise ValueError(f"El padron catastral debe ser >= {PADRON_CATASTRAL_MINIMO}.")

        # Superficie
        if not isinstance(superficie, (int, float)):
            raise ValueError("La superficie debe ser un número.")
        if superficie <= SUPERFICIE_MINIMA:
            raise ValueError(f"La superficie debe ser mayor a {SUPERFICIE_MINIMA} m².")

        # Domicilio
        if not isinstance(domicilio, str) or not domicilio.strip():
            raise ValueError("El domicilio debe ser una cadena no vacía.")

    # ======================================================
    # MODIFICACIÓN DE TIERRA
    # ======================================================
    def modificar_tierra(
        self,
        tierra: Tierra,
        nueva_superficie: float = None,
        nuevo_domicilio: str = None
    ) -> Tierra:
        """Modifica los atributos de una tierra existente."""

        if nueva_superficie is not None:
            if nueva_superficie <= SUPERFICIE_MINIMA:
                raise ValueError(f"La superficie debe ser mayor a {SUPERFICIE_MINIMA} m².")
            tierra.set_superficie(nueva_superficie)
            print(f"📐 Superficie de la tierra actualizada a {nueva_superficie} m²")

        if nuevo_domicilio is not None:
            if not nuevo_domicilio.strip():
                raise ValueError("El domicilio no puede estar vacío.")
            tierra.set_domicilio(nuevo_domicilio)
            print(f"🏠 Domicilio de la tierra actualizado a '{nuevo_domicilio}'")

        return tierra



################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 66
# Generado: 2025-10-22 12:08:04
################################################################################
