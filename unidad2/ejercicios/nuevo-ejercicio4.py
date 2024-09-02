import csv
import sys
from os.path import exists

# cotrolar la existecia del archivo
archivo = "calificaciones.csv"
if exists(archivo) is False:
    print(f"El archivo {archivo} o existe, el programa ha finalizado.")
    sys.exit(0)

# bucle principal del programa
while True:
    cotrol_menu = True

    # bulce de decisión del usuario
    while cotrol_menu:
        ingreso = input("ingrese I para ingresar un nuevo registro o S para salir")
        if ingreso == "S":
            print("cerrando el programa...")
            sys.exit(0)
        elif ingreso == "I":
            cotrol_menu = False
        else:
            print("error: las opciones son I para ingresar o S para salir")

    # print("si llegaste aca elegiste I")

    ingreso_apellido = True
    while ingreso_apellido:
        apellido = input("ingrese el apellido del alumno:")
        if len(apellido) >= 3 and len(apellido) <= 30:
            break
        print("error: el apellido debe tener entre 3 y 30 de caracteres")
