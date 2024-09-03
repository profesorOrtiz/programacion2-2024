import sys
import requests

r = requests.get("https://api.coincap.io/v2/assets/bitcoin")

if r.status_code != 200:
    print("Error, consulta no exitosa")
    sys.exit("Programa finalizado")

print(r.json())
