def suma(lista):
    return sum(lista)


try:
    assert suma([1, 1, 1]) == 3, "Deberia ser 3"
    assert suma([1, 1, 2]) != 3, "No deberia ser 3"
except AssertionError as e:
    print(f"El test ha fallado: {e}")
else:
    print("El test fue exitoso")