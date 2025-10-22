from typing import Dict, Type, TypeVar, Generic, List, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.servicios.negocio.paquete import Paquete

T = TypeVar('T', bound='Cultivo')


class FincasService:
    """
    Servicio de negocio para la administración y operaciones sobre múltiples fincas.
    Permite registrar fincas, fumigar, cosechar y obtener estadísticas generales.
    """

    def __init__(self):
        """Inicializa el servicio sin fincas registradas."""
        self._fincas: Dict[int, RegistroForestal] = {}  # ID padron -> RegistroForestal
        self._contador_paquetes: int = 0

    # ==================================================
    # MÉTODOS PRINCIPALES
    # ==================================================

    def add_finca(self, registro: 'RegistroForestal') -> None:
        
        id_padron = registro.get_id_padron()

        if id_padron in self._fincas:
            raise ValueError(f"Ya existe una finca con padrón {id_padron}")

        self._fincas[id_padron] = registro
        print(f"[FincasService] ✅ Finca agregada: {registro.get_propietario()} (Padrón {id_padron})")

    def buscar_finca(self, id_padron: int) -> 'RegistroForestal':
        
        if id_padron not in self._fincas:
            raise ValueError(f"No se encontró una finca con padrón {id_padron}")

        return self._fincas[id_padron]

    def fumigar(self, id_padron: int, plaguicida: str) -> None:
       
        finca = self.buscar_finca(id_padron)
        plantacion = finca.get_plantacion()

        if not plantacion:
            print(f"[FincasService] ⚠️ La finca con padrón {id_padron} no tiene plantación registrada.")
            return

        print(f"[FincasService] 🌿 Fumigando '{plantacion.get_nombre()}' con {plaguicida}...")
        print(f"[FincasService] ✅ Fumigación completada ({len(plantacion.get_cultivos())} cultivos tratados).")

    def cosechar_y_empaquetar(self, tipo_cultivo: Type[T]) -> Paquete[T]:
       
        cultivos_cosechados: List[T] = []
        print(f"[FincasService] 🚜 Iniciando cosecha de {tipo_cultivo.__name__}...")

        for registro in self._fincas.values():
            plantacion = registro.get_plantacion()
            if not plantacion:
                continue

            cultivos = plantacion.get_cultivos()
            cultivos_tipo = [c for c in cultivos if isinstance(c, tipo_cultivo)]
            cultivos_cosechados.extend(cultivos_tipo)

            # Nota: en una implementación completa, se debería eliminar o marcar los cultivos cosechados.
            if cultivos_tipo:
                print(f"  - {registro.get_propietario()}: {len(cultivos_tipo)} {tipo_cultivo.__name__} cosechados.")

        self._contador_paquetes += 1
        paquete = Paquete(id_paquete=self._contador_paquetes,tipo_cultivo=tipo_cultivo,cultivos=cultivos_cosechados
        )

        print(f"[FincasService] 📦 Total: {len(cultivos_cosechados)} {tipo_cultivo.__name__} empaquetados.")
        return paquete

    # ==================================================
    # MÉTODOS AUXILIARES
    # ==================================================

    def get_estadisticas(self) -> Dict:
       
        return {
            "total_fincas": len(self._fincas),
            "fincas_por_propietario": {
                registro.get_propietario(): registro.get_id_padron()
                for registro in self._fincas.values()
            },
            "total_paquetes_generados": self._contador_paquetes
        }

    def __str__(self) -> str:
        return f"FincasService(fincas={len(self._fincas)}, paquetes={self._contador_paquetes})"

