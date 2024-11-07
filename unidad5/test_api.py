import unittest
from unittest.mock import patch
from funciones_mock import obtener_datos


class TestApi(unittest.TestCase):
    # Indicamos que vamos a "parchear" el método requests.get que se encuentra dentro de el método obtener_datos
    @patch('requests.get')
    def test_obtener_datos(self, mock_get):
        # Simular la respuesta de la API para Bitcoin
        mock_get.return_value.json.return_value = {
            'data': {
                'id': 'bitcoin',
                'name': 'Bitcoin',
                'symbol': 'BTC',
                'priceUsd': '65000.00'
            }
        }

        # Llamar a la funcion con la URL (Nota: se va a interactuar con el mock en lugar de llamar a la API)
        resultado = obtener_datos('https://api.coincap.io/v2/assets/bitcoin')

        # Verificar que el resultado es el esperado
        resultado_esperado = {
            'data': {
                'id': 'bitcoin',
                'name': 'Bitcoin',
                'symbol': 'BTC',
                'priceUsd': '65000.00'
            }
        }
        self.assertEqual(resultado, resultado_esperado)

        # Verificar que el metodo requests.get fue llamado con la URL correcta
        mock_get.assert_called_once_with('https://api.coincap.io/v2/assets/bitcoin')


if __name__ == '__main__':
    unittest.main()
