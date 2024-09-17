import csv

encabezados = [
    'indice',
    'id',
    'nombre',
    'apellido',
    'genero',
    'email',
    'telefono',
    'fecha_nacimiento',
    'trabajo'
]
hombres = 0
mujeres = 0
with open('unidad2/people-100.csv') as f:
    archivo_csv = csv.DictReader(f, encabezados)
    # Saltear el encabezado
    next(archivo_csv)

    for linea in archivo_csv:
        if linea['genero'] == 'Male':
            hombres += 1 # hombres = hombres + 1
        else:
            mujeres += 1

print(f"Cantidad de hombres: {hombres}")
print(f"Cantidad de mujeres: {mujeres}")
