#h1
from python_forestacion.servicios.terrenos.tierra_service import TierraService

if __name__ == "__main__":
    tierra_service = TierraService()

    # Crear terreno
    terreno = tierra_service.crear_tierra_con_plantacion(
        id_padron_catastral=1,
        superficie=10000.0,
        domicilio="Agrelo, Mendoza",
        nombre_plantacion="Finca del Madero"
    )

    print(terreno)

    # Listar terrenos
    for t in tierra_service.listar_todos_los_terrenos():
        print(t)
# main.py

from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
#h2
def main():
    # Inicializamos los servicios
    tierra_service = TierraService()
    plantacion_service = PlantacionService()

    # Crear un terreno
    terreno = tierra_service.crear_tierra_con_plantacion(
        id_padron_catastral=1,
        superficie=10000.0,
        domicilio="Agrelo, Mendoza",
        nombre_plantacion=None  # Aún no tiene plantación
    )
    print("Terreno creado:", terreno)

    # Crear una plantación asociada a ese terreno
    plantacion = plantacion_service.crear_plantacion(
        terreno=terreno,
        nombre="Finca del Madero"
        # superficie=None → usa la del terreno
        # agua=500 → valor por defecto
    )
    print("Plantación creada:", plantacion)

    # Consultar plantaciones
    todas_las_plantaciones = plantacion_service.listar_plantaciones()
    print("Listado de todas las plantaciones:", todas_las_plantaciones)

if __name__ == "__main__":
    main()
