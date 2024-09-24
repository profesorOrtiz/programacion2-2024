def validarEdad(edad):
    if not isinstance(edad, int):
        raise ValueError("La edad debe ser un número entero")
    if edad < 0 or edad > 120:
        raise ValueError("La edad debe estar entre 0 y 120")


try:
    edad_input = input("Ingrese su edad:")
    edad = int(edad_input)
    validarEdad(edad)
except ValueError as error:
    print(error)
else:
    if edad < 18:
        print("Eres menor de edad")
    else:
        print("Eres mayor de edad")
