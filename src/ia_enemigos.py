import random
import sys
import time
from . import modulo_bolsa, estado, funciones
from colorama import init, Fore, Back, Style

personaje = estado.personaje


def creaEnemigo(vida, fuerza, nombreEnemigo):
    print(f'¡Apareció un {nombreEnemigo} de ultratumba!')
    print(f"¡Tiene {vida} puntos de vida!")
    while vida > 0:
        print("")
        accion = input("atacar o escapar: ").lower()
        if accion == "atacar":
            vida = vida - personaje["fuerza"]
            if vida <= 0:
                print(f'\n¡Has derrotado al {nombreEnemigo}!')
                print("Tu premio son 2 monedas (escudo +2)")
                personaje["escudo"] += 2
                time.sleep(1)
            else:
                print(f'Al {nombreEnemigo} le quedan {vida} puntos de vida')
                print(f'\n¡El {nombreEnemigo} ataca!')
                if personaje["escudo"] <= 0:
                    personaje["vida"] -= fuerza
                    if personaje["vida"] <= 0:
                        print("\n" + "*"*20)
                        print("      GAME OVER")
                        print("*"*20)
                        sys.exit()
                else:
                    personaje["escudo"] -= fuerza

            funciones.printEstado(personaje)
        elif accion == "escapar":
            print("\nEscapas por los pelos...")
            time.sleep(1)
            return
        else:
            print("No entiendo esa acción.")


def creaEnemigoAleatorio():
    enemigo = random.choice(["Esqueleto", "Murcielago", "Lobo"])
    loot = random.randint(1, 5)

    if loot % 2 == 0:

        if enemigo == 'Lobo':
            funciones.leer('src/ascii/lobo.dra', 'azul', True, True)

        loot_vida = random.randint(1, 20)
        loot_fuerza = random.randint(1, 4)
        creaEnemigo(loot_vida, loot_fuerza, enemigo)