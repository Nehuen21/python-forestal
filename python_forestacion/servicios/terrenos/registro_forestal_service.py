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
