import random
import sys
import time
from . import modulo_bolsa, estado, funciones
from colorama import init, Fore, Back, Style

personaje = estado.personaje


def creaEnemigo(vida, fuerza, nombreEnemigo):
    print('¡Aparecio un '+ nombreEnemigo +' de ultratumba!')
    print("¡Tiene", vida, "puntos de vida!")
    while vida > 0:
        print("")
        accion = input("atacar o escapar: ")
        if accion == "atacar":
            vida = vida - personaje["fuerza"]
            if vida <= 0:
                print('')
                print("Ganaste!!!!")
                print("Tu premio son 2 monedas")
                personaje["escudo"] += 2
            else:
                print('Al '+ nombreEnemigo +' le quedan ', vida, ' puntos de vida')
                print('')
                print('El '+ nombreEnemigo +' ataca!!!!')
                if personaje["escudo"] <= 0:
                    personaje["vida"] -= fuerza
                    if personaje["vida"] <= 0:
                        print("GAME OVER")
                        sys.exit()
                else:
                    personaje["escudo"] -= fuerza

            funciones.printEstado(personaje)
        else:
            print("Escapaste")
            return


def creaEnemigoAleatorio():
    enemigo = random.choice(["Esqueleto", "Murcielago", "Lobo"])
    loot = random.randint(1, 5)

    if loot % 2 == 0:

        if enemigo == 'Lobo':
            funciones.leer('src/ascii/lobo.dra', 'azul', True, True)

        loot_vida = random.randint(1, 20)
        loot_fuerza = random.randint(1, 4)
        creaEnemigo(loot_vida, loot_fuerza, enemigo)