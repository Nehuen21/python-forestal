from typing import List, TYPE_CHECKING
from datetime import date

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.constantes import AGUA_MINIMA_RIEGO


class PlantacionService:
    """Servicio encargado de la creación, control y mantenimiento de plantaciones."""

    def __init__(self):
        self._registry = CultivoServiceRegistry.get_instance()

    # ======================================================
    # CREACIÓN Y VALIDACIÓN
    # ======================================================
    def crear_plantacion(self, nombre: str, superficie: float, agua: int = 500) -> Plantacion:
        """
        Crea una nueva plantación aplicando las validaciones correspondientes.
        """
        self._validar_datos_plantacion(nombre, superficie, agua)

        plantacion = Plantacion(nombre=nombre, superficie=superficie, agua=agua)

        print(f"\n🌱 Plantación '{nombre}' creada con éxito")
        print(f"   → Superficie total: {superficie} m²")
        print(f"   → Agua inicial: {agua} L")
        return plantacion

    def _validar_datos_plantacion(self, nombre: str, superficie: float, agua: int) -> None:
        """Valida que los parámetros de la plantación sean correctos."""
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre de la plantación debe ser una cadena no vacía.")
        if not isinstance(superficie, (int, float)) or superficie <= 0:
            raise ValueError("La superficie debe ser un número positivo.")
        if not isinstance(agua, int) or agua < 0:
            raise ValueError("El agua disponible debe ser un número entero no negativo.")

    # ======================================================
    # CONTROL Y CONSULTA
    # ======================================================
    def obtener_plantacion_desde_tierra(self, tierra) -> Plantacion:
        """Retorna la plantación asociada a una tierra."""
        return tierra.get_finca()

    def controlar_superficie_ocupada(self, plantacion: Plantacion) -> tuple[float, float]:
        """Devuelve (superficie_ocupada, superficie_disponible)."""
        cultivos = plantacion.get_cultivos()
        superficie_ocupada = sum(c.get_superficie() for c in cultivos)
        superficie_disponible = plantacion.get_superficie() - superficie_ocupada
        return superficie_ocupada, superficie_disponible

    def get_estado_plantacion(self, plantacion: Plantacion) -> dict:
        """Obtiene un resumen del estado actual de la plantación."""
        superficie_ocupada, superficie_disponible = self.controlar_superficie_ocupada(plantacion)
        return {
            "nombre": plantacion.get_nombre(),
            "superficie_total": plantacion.get_superficie(),
            "superficie_ocupada": superficie_ocupada,
            "superficie_disponible": superficie_disponible,
            "agua_disponible": plantacion.get_agua(),
            "cantidad_cultivos": len(plantacion.get_cultivos()),
            "cantidad_trabajadores": len(plantacion.get_trabajadores())
        }

    # ======================================================
    # AGREGAR CULTIVOS
    # ======================================================
    def agregar_cultivo_a_plantacion(self, plantacion: Plantacion, cultivo: 'Cultivo') -> None:
        """
        Agrega un solo cultivo a la plantación, verificando superficie disponible.
        """
        superficie_cultivo = cultivo.get_superficie()
        _, superficie_disponible = self.controlar_superficie_ocupada(plantacion)

        if superficie_cultivo > superficie_disponible:
            raise SuperficieInsuficienteException(
                user_message=f"Superficie insuficiente para agregar {cultivo.__class__.__name__}",
                technical_message=f"Requerida: {superficie_cultivo}m², Disponible: {superficie_disponible:.2f}m²",
                superficie_requerida=superficie_cultivo,
                superficie_disponible=superficie_disponible
            )

        plantacion.agregar_cultivo(cultivo)
        print(f"🌾 Cultivo '{cultivo.__class__.__name__}' agregado a la plantación '{plantacion.get_nombre()}'")

    def plantar(self, plantacion: Plantacion, especie: str, cantidad: int) -> List[Cultivo]:
        """
        Planta múltiples cultivos de una especie específica.
        """
        if cantidad <= 0:
            raise ValueError("La cantidad a plantar debe ser mayor que cero.")

        cultivos_creados = [CultivoFactory.crear_cultivo(especie) for _ in range(cantidad)]
        superficie_requerida = sum(c.get_superficie() for c in cultivos_creados)
        _, superficie_disponible = self.controlar_superficie_ocupada(plantacion)

        if superficie_requerida > superficie_disponible:
            raise SuperficieInsuficienteException(
                user_message=f"No hay superficie suficiente para plantar {cantidad} {especie}(s).",
                technical_message=f"Requerida: {superficie_requerida}m², Disponible: {superficie_disponible}m²",
                superficie_requerida=superficie_requerida,
                superficie_disponible=superficie_disponible
            )

        plantacion.agregar_cultivos(cultivos_creados)

        print(f"\n🌾 Se plantaron {cantidad} {especie}(s) en '{plantacion.get_nombre()}'")
        print(f"   → Superficie utilizada: {superficie_requerida:.2f} m²")
        print(f"   → Superficie restante: {superficie_disponible - superficie_requerida:.2f} m²")
        return cultivos_creados

    def obtener_cultivos_por_tipo(self, plantacion: Plantacion, especie: type) -> List[Cultivo]:
        """Devuelve una lista de cultivos del tipo especificado."""
        return [c for c in plantacion.get_cultivos() if isinstance(c, especie)]

    # ======================================================
    # AGUA Y RIEGO
    # ======================================================
    def set_agua_disponible(self, plantacion: Plantacion, agua: int) -> None:
        """Actualiza el agua disponible en la plantación."""
        if agua < 0:
            raise ValueError("El agua disponible no puede ser negativa.")
        plantacion.set_agua(agua)
        print(f"💧 Agua disponible actualizada a {agua} L para '{plantacion.get_nombre()}'")

    def regar(self, plantacion: Plantacion, fecha: date = None, temperatura: float = 20.0, humedad: float = 50.0) -> dict:
        """Riega todos los cultivos de la plantación distribuyendo el agua."""
        if fecha is None:
            fecha = date.today()

        agua_disponible = plantacion.get_agua()
        if agua_disponible < AGUA_MINIMA_RIEGO:
            raise AguaAgotadaException(
                user_message="No hay suficiente agua para realizar el riego.",
                technical_message=f"Disponible: {agua_disponible}L, Requerido: {AGUA_MINIMA_RIEGO}L",
                agua_disponible=agua_disponible,
                agua_requerida=AGUA_MINIMA_RIEGO
            )

        plantacion.set_agua(agua_disponible - AGUA_MINIMA_RIEGO)
        cultivos = plantacion.get_cultivos()

        resumen = {
            "agua_consumida": AGUA_MINIMA_RIEGO,
            "cultivos_regados": len(cultivos),
            "agua_absorbida_total": 0,
            "detalle_por_tipo": {}
        }

        for cultivo in cultivos:
            absorbida = self._registry.absorber_agua(cultivo, fecha, temperatura, humedad)
            self._registry.hacer_crecer(cultivo)
            resumen["agua_absorbida_total"] += absorbida

            tipo = cultivo.__class__.__name__
            detalle = resumen["detalle_por_tipo"].setdefault(tipo, {"cantidad": 0, "agua_absorbida": 0})
            detalle["cantidad"] += 1
            detalle["agua_absorbida"] += absorbida

        print(f"\n💦 Riego realizado en '{plantacion.get_nombre()}' ({len(cultivos)} cultivos)")
        print(f"   → Agua consumida: {AGUA_MINIMA_RIEGO} L")
        print(f"   → Total absorbido por cultivos: {resumen['agua_absorbida_total']:.2f} L")
        return resumen

    # ======================================================
    # VISUALIZACIÓN
    # ======================================================
    def mostrar_datos_cultivos(self, plantacion: Plantacion) -> None:
        """Muestra los cultivos de la plantación con información resumida."""
        cultivos = plantacion.get_cultivos()

        if not cultivos:
            print("\n⚠️ No hay cultivos registrados en esta plantación.")
            return

        print(f"\n🌿 Cultivos registrados en '{plantacion.get_nombre()}' ({len(cultivos)} total)")
        print("=" * 55)
        for i, cultivo in enumerate(cultivos, 1):
            print(f"\n[{i}] {cultivo.__class__.__name__}")
            self._registry.mostrar_datos(cultivo)
        print("=" * 55)
