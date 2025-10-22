import unittest
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.servicios.terrenos.tierra_service import TierraService

class TestTierraService(unittest.TestCase):

    def setUp(self):
        # Se ejecuta antes de cada test
        self.service = TierraService()

    def test_crear_tierra_valida(self):
        tierra = self.service.crear_tierra_con_plantacion(
            id_padron_catastral=1,
            superficie=10000.0,
            domicilio="Agrelo, Mendoza",
            nombre_plantacion="Finca del Madero"
        )
        self.assertEqual(tierra.id_padron_catastral, 1)
        self.assertEqual(tierra.superficie, 10000.0)
        self.assertEqual(tierra.domicilio, "Agrelo, Mendoza")
        self.assertEqual(tierra.nombre_plantacion, "Finca del Madero")

    def test_superficie_invalida(self):
        # Superficie <= 0 debe lanzar ValueError
        with self.assertRaises(ValueError):
            self.service.crear_tierra_con_plantacion(
                id_padron_catastral=2,
                superficie=0,
                domicilio="Agrelo, Mendoza"
            )
        with self.assertRaises(ValueError):
            self.service.crear_tierra_con_plantacion(
                id_padron_catastral=3,
                superficie=-500,
                domicilio="Agrelo, Mendoza"
            )

    def test_padron_unico(self):
        # Crear un terreno
        self.service.crear_tierra_con_plantacion(
            id_padron_catastral=1,
            superficie=1000,
            domicilio="Agrelo"
        )
        # Intentar crear otro con mismo padron que no seria valido
        with self.assertRaises(ValueError):
            self.service.crear_tierra_con_plantacion(
                id_padron_catastral=1,
                superficie=2000,
                domicilio="Tunuyán"
            )

    def test_modificar_superficie(self):
        # Crear terreno
        tierra = self.service.crear_tierra_con_plantacion(
            id_padron_catastral=5,
            superficie=1500,
            domicilio="Lujan"
        )
        # Modificar una superficie que si es valida
        tierra.set_superficie(2000)
        self.assertEqual(tierra.superficie, 2000)

        # Modificar una superficie invalida
        with self.assertRaises(ValueError):
            tierra.set_superficie(0)
        with self.assertRaises(ValueError):
            tierra.set_superficie(-10)

if __name__ == "__main__":
    unittest.main()
