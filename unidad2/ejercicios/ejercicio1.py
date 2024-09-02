# Verificar si el número ingresado está entre 1 y 10
def pedir_numero():
    while True:
        try:
            numero = int(input("Ingrese un numero entre 1 y 10: "))
            if 1 <= numero <= 10:
                return numero
            else:
                print("El numero no está en el rango. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un numero válido.")


# Crear o sobrescribir el archivo tabla.txt con la tabla de multiplicar
def crear_tabla(numero):
    # Controlar si el archivo existe; caso contrario,
    # crear el archivo tabla.txt
    with open("tabla.txt", "w") as archivo:
        for i in range(1, 11):
            archivo.write(f"{i} x {numero} = {i*numero}\n")


# Programa principal
if __name__ == "__main__":
    numero = pedir_numero()
    crear_tabla(numero)
