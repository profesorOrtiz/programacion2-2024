print("Procesando operacion")
try:
    print(1/0)
except ZeroDivisionError as error:
    print("Ocurrio un error al procesar la operacion")
print("Operacion finalizada")