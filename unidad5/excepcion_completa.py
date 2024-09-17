print("Procesando operacion")
try:
    print(1/0)
except ZeroDivisionError as error:
    print("Ocurrio un error al procesar la operacion")
else: # Se ejecuta si no hubo un error en el try
    try:
        with open("archivo.txt") as archivo:
            datos = archivo.read()
    except FileNotFoundError as archivo_error:
        print("Ocurrio un error al abrir el archivo")
    finally:
        print("Tareas de limpieza de archivo")
finally: # Se ejecuta siempre, con o sin error
    print("Tareas de limpieza")
print("Operacion finalizada")