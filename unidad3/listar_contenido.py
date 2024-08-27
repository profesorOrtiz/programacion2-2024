archivo = open('data.txt')
# Opcion 1
# contenido = archivo.readlines()
# print(contenido)
# Opcion 2
contenido = list(archivo)
print(contenido)
# Cerrar el archivo cuando ya no lo usemos
archivo.close()