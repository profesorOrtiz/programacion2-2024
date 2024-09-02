lista_compra = {'manzana', 'naranja', 'pera', 'banana', 'leche', 'harina', 'azucar'}
canasta_compra = {'harina', 'manzana', 'naranja', 'papel higienico', 'azucar'}

# 1) Obtener un listado de los productos que estaban en la lista pero no pudieron ser comprados
productos_no_comprados = lista_compra - canasta_compra

for producto in productos_no_comprados:
    print(producto)

# 2) Obtener un listado de los productos que estaban en la lista y también fueron comprados
lista_canasta = lista_compra & canasta_compra
print(lista_canasta)

# 3) Obtener un listado de los productos que fueron comprados sin haber estado previamente en la lista
compra_espontanea = canasta_compra - lista_compra
print(compra_espontanea)
