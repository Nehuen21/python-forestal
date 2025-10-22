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
