print("Procesando operacion")
try:
    print(1/0)
    with open("archivo.txt") as archivo:
        datos = archivo.read()
except ZeroDivisionError as error:
    print("Ocurrio un error al procesar la operacion")
except FileNotFoundError as archivo_error:
    print("Ocurrio un error al abrir el archivo")
print("Operacion finalizada")