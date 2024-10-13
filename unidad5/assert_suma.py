def suma(lista):
    return sum(lista)


assert suma([1, 1, 1]) == 3, "Deberia ser 3"
assert suma([1, 1, 2]) != 3, "No deberia ser 3"