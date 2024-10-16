import unittest

from funciones import es_primo

class TestPrimo(unittest.TestCase):
    # TODO: definir test
    def test_numero_primo(self):
        """ Comprobar que 17 es un numero primo """
        self.assertTrue(es_primo(17))

    # TODO: definir test
    @unittest.skip("Falta implementar comprobacion de numero no primo")
    def test_numero_no_primo(self):
        """ Comprobar que 10 no es un numero primo """
        self.assertFalse(es_primo(10))

if __name__ == "__main__":
    unittest.main(verbosity=2)
