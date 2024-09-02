import csv

with open('unidad2/people-100.csv', 'r') as f:
    # Leer la línea del CSV y devolver una lista
    archivo_csv = csv.reader(f)
    for num_linea, linea in enumerate(archivo_csv, 1):
        if num_linea == 1:
            print("Encabezado")
            print(linea)
            print("\n")
        else:
            print(linea)
