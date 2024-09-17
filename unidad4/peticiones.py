import sys
import requests
from datetime import datetime

r = requests.get("https://api.coincap.io/v2/assets")

if r.status_code != 200:
    print("Error, consulta no exitosa")
    sys.exit("Programa finalizado")

datos = r.json()
cotizaciones = datos['data']
fecha = datetime.fromtimestamp(datos['timestamp'] / 1e3)

print("{:<25}|{:<8}|{:>25}".format("Moneda", "Simbolo", "Precio (USD)"))
print("-"*60)

for cotizacion in cotizaciones:
    linea = "{:<25}|{:<8}|{:>25}".format(
        cotizacion['id'],
        cotizacion['symbol'],
        cotizacion['priceUsd']
    )
    print(linea)

print(f"Fecha de consulta: {fecha}")
