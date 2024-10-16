import unittest

from funciones import (
    sumar,
    restar,
    dividir,
    multiplicar,
    promedio,
    mediana,
    moda
)

class TestOperacionesAritmeticas(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(10, 5), 15)
        self.assertEqual(sumar(-1, 1), 0)

    def test_restar(self):
        self.assertEqual(restar(10, 5), 5)
        self.assertEqual(restar(-1, 1), -2)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(10, 5), 50)
        self.assertEqual(multiplicar(-1, 1), -1)

    def test_dividir(self):
        self.assertEqual(dividir(10, 5), 2)
        self.assertEqual(dividir(-1, 1), -1)
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)

class TestOperacionesEstadisticas(unittest.TestCase):
    def test_promedio(self):
        self.assertEqual(promedio([1, 2, 3, 4, 5, 6]), 3.5)

    def test_mediana(self):
        self.assertEqual(mediana([1, 3, 3, 6, 7, 8, 9]), 6)

    def test_moda_simple(self):
        self.assertEqual(moda([1, 2, 2, 3, 4, 4, 4, 5]), [4])

    def test_moda_multiple(self):
        self.assertEqual(set(moda([1, 1, 2, 3, 4, 4, 5, 5])), {1, 4, 5})

# TODO: agregar load_tests()
def load_tests(loader, standard_tests, pattern):
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestOperacionesAritmeticas))
    suite.addTests(loader.loadTestsFromTestCase(TestOperacionesEstadisticas))
    return suite

if __name__ == "__main__":
    unittest.main(verbosity=2)
