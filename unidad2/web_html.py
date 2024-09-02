from urllib.request import urlopen

web = urlopen("https://www.recursospython.com")
with open("recursospython.html", "wb") as f:
    f.write(web.read())

web = urlopen("https://www.google.com")
with open("google.html", "wb") as f:
    f.write(web.read())

print("Se ha guardado el contenido de las páginas en sus archivos HTML")
