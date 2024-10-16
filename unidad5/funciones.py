import math
from collections import Counter

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True

def generar_multiplos_pares(numero):
    lista = []
    for i in range(numero, 1000, numero):
        if len(lista) == 5:
            break
        if i % 2 == 0:
            lista.append(i)
    return lista

def generar_conjunto():
    conjunto = set()
    for i in range(1, 6):
        conjunto.add(i)
    return conjunto

def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        raise ZeroDivisionError("No se puede dividir por cero.")
    return x / y

def promedio(datos):
    return sum(datos) / len(datos)

def mediana(datos):
    n = len(datos)
    indice = n // 2
    if n % 2:
        return sorted(datos)[indice]
    return sum(sorted(datos)[indice - 1 : indice + 1]) / 2

def moda(datos):
    c = Counter(datos)
    return [k for k, v in c.items() if v == c.most_common(1)[0][1]]