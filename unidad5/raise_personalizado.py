from EdadInvalidaError import EdadInvalidaError


def validarEdad(edad):
    if not isinstance(edad, int):
        raise EdadInvalidaError("La edad debe ser un número entero")
    if edad < 0 or edad > 120:
        raise EdadInvalidaError("La edad debe estar entre 0 y 120")


while True:
    try:
        edad_input = input("Ingrese su edad:")
        # -> 1° punto de error: ValueError
        edad = int(edad_input)
        # -> 2° punto de error: EdadInvalidaError
        validarEdad(edad)
        if edad < 18:
            print("Eres menor de edad")
        else:
            print("Eres mayor de edad")
        break
    except ValueError:
        print("Error: el dato ingresado debe ser un número entero")
    except EdadInvalidaError as error:
        print(f"Error: {error}")
