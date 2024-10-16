import unittest

from funciones import generar_conjunto, generar_multiplos_pares

class TestSecuencias(unittest.TestCase):
    # TODO: definir test
    def test_igualdad_conjunto(self):
        # conjunto = {1, 2, 3, 4, 5}
        # resultado_funcion = generar_conjunto()
        self.assertSetEqual(generar_conjunto(), {1, 2, 3, 4, 5})

    # TODO: definir test
    def test_igualdad_lista(self):
        lista = [6, 12, 18, 24, 30]
        self.assertListEqual(generar_multiplos_pares(3), lista)

if __name__ == "__main__":
    unittest.main(verbosity=2)
