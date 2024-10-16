import unittest

class TestIdentidad(unittest.TestCase):
    # TODO: definir test
    def test_listas_mismo_tipo(self):
        a = ["Python", "PHP"]
        b = a
        self.assertIs(a, b)

    # TODO: definir test
    def test_distintas_listas(self):
        a = ["Python", "PHP"]
        b = ["Python", "PHP"]
        self.assertIsNot(a, b)

    # TODO: definir test
    def test_listas_no_vacias(self):
        a = ["Python", "PHP"]
        self.assertIsNotNone(a)

if __name__ == "__main__":
    unittest.main(verbosity=2)
