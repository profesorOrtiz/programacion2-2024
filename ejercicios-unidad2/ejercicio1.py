from math import sqrt
# Formula = peso / altura2
peso = int(input("Ingrese su peso en kilogramos: "))
altura = int(input("Ingrese su altura en centímetros: "))
altura = float(altura)
imc = peso / sqrt(altura)
print(imc)