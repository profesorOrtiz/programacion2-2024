import math


# Formula de variacion porcentual
# ((valor final - valor inicial) / valor inicial) * 100
def variacion_porcentual(valor_inicial, valor_final):
    variacion = ((valor_final - valor_inicial) / valor_inicial) * 100
    # Si el resultado es entero, convertirlo a un entero puro
    if variacion.is_integer():
        variacion = (int)(math.fabs(variacion))
    # Si el resultado es decimal, redondear a 2 decimales
    else:
        variacion = round(math.fabs(variacion), 2)
    return variacion


vi = 100
vf = 110
porcentaje = variacion_porcentual(vi, vf)
print(f"La variacion porcentual entre {vi} y {vf} es {porcentaje}%")
