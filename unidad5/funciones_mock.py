import requests


def obtener_datos(url):
    respuesta = requests.get(url)
    return respuesta.json()


def sumar(x, y):
    return x + y


class Lista:
    def __init__(self):
        self.items = []

    def agregar(self, item):
        self.items.append(item)

    def leer(self):
        return self.items

    def limpiar(self):
        self.items.clear()
