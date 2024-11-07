from suma import suma
import unittest


class TestSuma(unittest.TestCase):
    def test_suma_ideal(self):
        # assert suma([1, 1, 1]) == 3, "Deberia ser 3"
        self.assertEqual(suma([1, 1, 1]), 3, "Deberia ser 3")

    def test_suma_incorrecto(self):
        self.assertNotEqual(suma([1, 1, 2]), 3, "Deberia ser 4")

if __name__ == '__main__':
    unittest.main()
