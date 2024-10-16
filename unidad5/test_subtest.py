import unittest

from funciones import es_primo

class TestSubtest(unittest.TestCase):
    # TODO: definir el test
    def test_numero_primo(self):
        """ Comprobar si una lista de numeros son numeros primos """
        for numero in [2, 7, 17]:
            with self.subTest(numero=numero):
                self.assertTrue(es_primo(numero))

    # TODO: definir el test
    def test_numero_no_primo(self):
        """ Comprobar si una lista de numeros no son numeros primos """
        for numero in [4, 6, 8]:
            with self.subTest(numero=numero):
                self.assertFalse(es_primo(numero))

if __name__ == "__main__":
    unittest.main(verbosity=2)
