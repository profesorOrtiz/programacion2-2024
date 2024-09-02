import csv

hombres = 0
mujeres = 0
with open('people-100.csv') as f:
    archivo_csv = csv.reader(f)
    # Saltear el encabezado
    next(archivo_csv)

    for linea in archivo_csv:
        if linea[4] == 'Male':
            hombres += 1 # hombres = hombres + 1
        else:
            mujeres += 1

print(f"Cantidad de hombres: {hombres}")
print(f"Cantidad de mujeres: {mujeres}")
