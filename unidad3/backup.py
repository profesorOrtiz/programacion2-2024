# Este programa lee los datos de un archivo y realiza una copia en el archivo secundario o de backup
archivo_original = 'files/data_original.txt'
archivo_backup = 'files/data_backup.txt'
with open(archivo_original) as ori, open(archivo_backup, 'w') as bac:
    # Leemos todas las lineas del archivo original
    datos_originales = ori.readlines()
    # Insertamos las lineas en el archivo backup
    bac.writelines(datos_originales)

print("El backup se realizó con éxito")