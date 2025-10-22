import unittest
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService

class TestPlantacionService(unittest.TestCase):

    def setUp(self):
        # Inicializamos los servicios
        self.tierra_service = TierraService()
        self.plantacion_service = PlantacionService()

        # Creamos un terreno válido
        self.terreno = self.tierra_service.crear_tierra_con_plantacion(
            id_padron_catastral=1,
            superficie=10000.0,
            domicilio="Agrelo, Mendoza"
        )

    def test_crear_plantacion_valida(self):
        # Crear plantación con valores por defecto
        plantacion = self.plantacion_service.crear_plantacion(
            terreno=self.terreno,
            nombre="Finca del Madero"
        )
        self.assertEqual(plantacion.nombre, "Finca del Madero")
        self.assertEqual(plantacion.superficie, self.terreno.superficie)
        self.assertEqual(plantacion.agua_disponible, 500)
        self.assertEqual(plantacion.cultivos, [])
        self.assertEqual(plantacion.trabajadores, [])
        self.assertEqual(plantacion.terreno, self.terreno)

    def test_agua_no_negativa(self):
        plantacion = self.plantacion_service.crear_plantacion(
            terreno=self.terreno,
            nombre="Finca Agua"
        )
        # Agua válida
        plantacion.set_agua_disponible(1000)
        self.assertEqual(plantacion.agua_disponible, 1000)
        # Agua inválida
        with self.assertRaises(ValueError):
            plantacion.set_agua_disponible(-50)

    def test_plantacion_asociada_a_terreno_invalido(self):
        # Intentar asociar None como terreno
        with self.assertRaises(ValueError):
            self.plantacion_service.crear_plantacion(
                terreno=None,
                nombre="Plantacion Fantasma"
            )

    def test_listar_plantaciones(self):
        plantacion1 = self.plantacion_service.crear_plantacion(
            terreno=self.terreno,
            nombre="Plantacion 1"
        )
        plantacion2 = self.plantacion_service.crear_plantacion(
            terreno=self.terreno,
            nombre="Plantacion 2"
        )
        todas = self.plantacion_service.listar_plantaciones()
        self.assertIn(plantacion1, todas)
        self.assertIn(plantacion2, todas)
        self.assertEqual(len(todas), 2)

if __name__ == "__main__":
    unittest.main()
