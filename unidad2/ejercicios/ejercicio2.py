with open('clientes.txt', 'r') as f:
    lineas = f.readlines()
    clientes = []
    for linea in lineas:
        data = linea.strip().split(',')
        dni = int(data[3])
        if dni < 40000000:
            clientes.append(data)
        clientes.sort(key=lambda x: x[2])
    for cliente in clientes:
        print(f"El cliente {cliente[0]} se llama {cliente[1]} {cliente[2]} y"
              f" su DNI es {cliente[3]}")
