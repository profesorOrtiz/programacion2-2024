import unittest

from vehiculos import Auto, Camioneta

class TestVehiculos(unittest.TestCase):
    def test_auto_es_instancia_de_vehiculo(self):
        auto = Auto("Chevrolet", "Corvette", 194)
        self.assertIsInstance(auto, Auto)

    def test_camioneta_es_instancia_de_vehiculo(self):
        camioneta = Camioneta("Ford", "F-150", 2000)
        self.assertNotIsInstance(camioneta, Auto)

if __name__ == "__main__":
    unittest.main(verbosity=2)
