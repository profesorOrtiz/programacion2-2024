import unittest
from funciones_mock import Lista


class TestLista(unittest.TestCase):
    def setUp(self):
        """Método que se ejecuta antes de cada prueba"""
        self.lista = Lista()

    def tearDown(self):
        """Método que se ejecuta después de cada prueba"""
        self.lista.limpiar()

    def test_agregar_elemento(self):
        self.lista.agregar(1)
        self.assertEqual(self.lista.leer(), [1])

    def test_agregar_varios_elementos(self):
        self.lista.agregar(1)
        self.lista.agregar(2)
        self.assertEqual(self.lista.leer(), [1, 2])

    def test_limpiar_lista(self):
        self.lista.agregar(1)
        self.lista.limpiar()
        self.assertEqual(self.lista.leer(), [])


if __name__ == "__main__":
    unittest.main()
