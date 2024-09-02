import csv

with open('people-100.csv', 'r') as f:
    # Leer la línea del CSV y devolver una lista
    archivo_csv = csv.reader(f)
    for linea in archivo_csv:
        print(linea)
