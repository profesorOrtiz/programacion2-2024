while True:
    try:
        edad = int(input('ingrese su edad:'))
    except ValueError:
        print('Por favor ingrese una edad en números')
    else:
        break

print(f'tienes {edad} años')
