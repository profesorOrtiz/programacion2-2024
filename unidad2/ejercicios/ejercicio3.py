import csv
import sys
from os.path import exists

aprobados = []
desaprobados = []

try:
    # Comprobar la existencia del archivo CSV
    archivo = 'calificaciones.csv'
    if exists(archivo) == False:
        print(f"El archivo {archivo} no existe, el programa ha finalizado.")
        # Finalizar el programa enviando la señal de cierre al sistema
        sys.exit(0)

    with open('calificaciones.csv', 'r') as f:
        archivo_csv = csv.DictReader(f, delimiter=';')

        for linea in archivo_csv:
            # Verificar si las columnas necesarias están presentes en la fila
            if 'Parcial1' in linea and 'Parcial2' in linea and 'Asistencia' in linea:
                if int(linea["Parcial1"]) >= 6 and int(linea["Parcial2"]) >= 6 and int(linea["Asistencia"]) >= 75:
                    aprobados.append(f'{linea["Apellido"]}, {linea["Nombre"]}')
                else:
                    motivo_desaprobado = []
                    if int(linea["Parcial1"]) < 6:
                        motivo_desaprobado.append(f'desaprobado el Parcial 1 con nota {linea["Parcial1"]}')
                    if int(linea["Parcial2"]) < 6:
                        motivo_desaprobado.append(f'desaprobado el Parcial 2 con nota {linea["Parcial2"]}')
                    if int(linea["Asistencia"]) < 75:
                        motivo_desaprobado.append('asistencia insuficiente')
                    desaprobados.append(f'{linea["Apellido"]}, {linea["Nombre"]}: {", ".join(motivo_desaprobado)}')
            else:
                print("Error: Faltan datos en la fila del archivo csv.")

    print("ALUMNOS APROBADOS")
    for alumno in aprobados:
        print(f'- {alumno}')

    print("\nALUMNOS DESAPROBADOS")
    for alumno in desaprobados:
        print(f'- {alumno}')
except Exception as e:
    print(f"Se produjo una excepción: {e}")
