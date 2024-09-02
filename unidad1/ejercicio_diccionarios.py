salarios = {
    'juan': 450000,
    'pedro': 250000,
    'daniela': 365000,
    'daiana': 750000,
    'gimena': 500000
}

excelente = 0
bueno = 0
malo = 0

for salario in salarios.values():
    if salario >= 500000:
        excelente += 1
    elif 300000 <= salario <= 499999:
        bueno += 1
    else:
        malo += 1

print("Trabajadores con salario Excelente:", excelente)
print("Trabajadores con salario Bueno:", bueno)
print("Trabajadores con salario Malo:", malo)
