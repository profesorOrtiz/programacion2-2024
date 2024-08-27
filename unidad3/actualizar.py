"""
Leer el archivo clientes.txt y mostrar los clientes cuyos DNI sean mayores a 40.000.000
"""
def actualizar():
    with open('data.txt', 'a') as f:
        data = "Honduras\n"
        f.write(data)

    print("Se ha ingresado el nuevo dato")