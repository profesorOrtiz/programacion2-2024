import csv
import sys
from os.path import exists

# Controlar la existencia del archivo
archivo = 'calificaciones.csv'
if exists(archivo) == False:
    print(f"El archivo {archivo} no existe, el programa ha finalizado.")
    sys.exit(0)

# Bucle principal del programa
while True:
    control_menu = True
    # Bucle de decision del usuario
    while control_menu:
        ingreso = input("Ingrese I para ingresar un nuevo registro o S para salir")
        if ingreso.upper() == 'S':
            print("Cerrando el programa...")
            sys.exit(0)
        elif ingreso.upper() == 'I':
            control_menu = False
        else:
            print("Error: las opciones son I para ingresar o S para salir")

    # print("Si llegaste aca elegiste I")
    # Pedir los ingresos de los 5 datos y validarlos
    ingreso_apellido = True
    while ingreso_apellido:
        apellido = input("Ingrese el apellido del alumno: ")
        if len(apellido) >= 3 and len(apellido) <= 30:
            break
        print("Error: el apellido debe tener entre 3 y 30 caracteres")

    print("Si llegaste aca el apellido es correcto")
