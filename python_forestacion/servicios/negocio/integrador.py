"""
Archivo integrador generado automaticamente
Directorio: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/negocio
Fecha: 2025-10-22 12:08:04
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/negocio/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: fincas_service.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/negocio/fincas_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: paquete.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/negocio/paquete.py
# ================================================================================

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

