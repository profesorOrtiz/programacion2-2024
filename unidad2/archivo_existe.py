from os.path import exists

# 1) Comprobar si el archivo a usar existe
archivo = 'unidad2/archivo.txt'
if exists(archivo):
    # 2) Si existe, lo abrimos en el modo w, sino en el modo x
    modo = 'w'
else:
    modo = 'x'

# 3) Trabajamos con el archivo
with open(archivo, modo) as f:
    f.write('Nueva linea de texto')
