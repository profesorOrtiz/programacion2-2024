import unittest

from funciones import generar_multiplos_pares

class TestMultiplosPares(unittest.TestCase):
    # TODO: definir test
    def test_tiene_numero_seis(self):
        self.assertIn(6, generar_multiplos_pares(3))

    # TODO: definir test
    def test_no_tiene_numero_sesenta(self):
        self.assertNotIn(60, generar_multiplos_pares(3))

    # TODO: definir test
    def test_no_tiene_numero_impar(self):
        self.assertNotIn(9, generar_multiplos_pares(3))

if __name__ == "__main__":
    unittest.main(verbosity=2)
