colores = input("Ingresa 3 colores separados por comas")
lista_colores = colores.split(',')
for color in lista_colores:
    print(color.strip())
