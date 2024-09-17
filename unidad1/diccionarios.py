lista_correo = {
    'juan': 'juan@mail.com',
    'pedro': 'pedro@mail.com',
    'daniela': 'daniela@mail.com',
    'daiana': 'daiana@mail.com',
    'gimena': 'gimena@mail.com',
    'david': 'david@mail.com'
}
lista_correo['gimena'] = 'gimennnna@mail.com'
del lista_correo['daniela']
# print(lista_correo.items())
# print(lista_correo.keys())
# print(lista_correo.values())

for clave, valor in lista_correo.items():
    print("El usuario " + clave + " tiene su correo: " + valor)
