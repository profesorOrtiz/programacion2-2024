import sys
from random import randint

hp_personaje = 20
enemigos = list()

for i in range(10):
    enemigos.append(randint(1, 4))

print(f"Bienvenido al juego de rol y aventura. Inicias con tu personaje con {hp_personaje} puntos de vida")
while True:
    ingreso = input("Ingresa A para arrojar el dado o S para salir")
    if(ingreso.lower() == 'S'):
        print("Saliendo del programa")
        sys.exit(0)
    else:
        dado = randint(1, 3)
        if dado == 1:
            pocion = randint(1, 2)
            if hp_personaje >= 20:
                print(f"Te encontraste con una poción que no tuvo efecto, ya cuentas con la salud máxima de {hp_personaje} HP")
            else:
                hp_personaje += pocion
                print(f"Te encontraste con una poción que restaura {pocion} HP, tus puntos de vida actuales son {hp_personaje}")
        elif dado == 2:
            print("Te has tomado un descanso, pasas a la siguiente ronda")
        elif dado == 3:
            enemigo = enemigos.pop(0)
            hp_personaje -= enemigo
            print(f"Te encontraste con un enemigo que inflije {enemigo} HP, tus puntos de vida actuales son {hp_personaje}")
            if hp_personaje <= 0:
                print("Tu personaje ya no cuenta con mas HP, el juego ha terminado en DERROTA")
                sys.exit(0)