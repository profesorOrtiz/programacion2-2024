def suma(*args):
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado

print(suma(2, 4))
print(suma(2, 4, 8, 10))
print(suma(2, 4, 8, 10, 12, 23, 34))