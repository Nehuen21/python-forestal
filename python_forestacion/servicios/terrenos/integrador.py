"""
Archivo integrador generado automaticamente
Directorio: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/terrenos
Fecha: 2025-10-22 12:08:04
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/terrenos/__init__.py
# ================================================================================

"""Servicios de dominio relacionados con terrenos, tierras, plantaciones y registros forestales."""

from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService

__all__ = [
    "TierraService",
    "PlantacionService",
    "RegistroForestalService"
]


# ================================================================================
# ARCHIVO 2/4: plantacion_service.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/terrenos/plantacion_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/4: registro_forestal_service.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/terrenos/registro_forestal_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/4: tierra_service.py
# Ruta: /home/nehuen/Escritorio/ParcialAhora/python-forestal/python_forestacion/servicios/terrenos/tierra_service.py
# ================================================================================

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


