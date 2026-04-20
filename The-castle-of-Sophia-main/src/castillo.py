import random
import time
import sys
from colorama import Fore
from . import funciones, estado, ia_enemigos, menus

def entrada():
    estado.ubicacion_personaje['posicion'] = 'castillo_entrada'
    funciones.borrarPantalla()
    print(Fore.RED + '--- ENTRADA DEL CASTILLO ---')
    print('')
    print(Fore.GREEN + " Una niebla intensa dificulta la visibilidad.")
    print(Fore.GREEN + " Hay una gran puerta de madera al norte")
    print(Fore.GREEN + " Al sur vuelves a cruzar el puente")
    print('')

    opcion = input(Fore.YELLOW + "¿norte o sur? ")
    
    if opcion == 'norte': 
        return 'castillo_room1'
    elif opcion == 'sur':
        return 'fuera_puente'
    else:
        print(Fore.RED + 'No puedes ir por ahí.')
        time.sleep(1)
        return 'castillo_entrada'

# ROOM 1 --------------------------------------------------------------------------

def room1():
    estado.ubicacion_personaje['posicion'] = 'castillo_room1' 
    funciones.borrarPantalla()
    print(Fore.RED + '--- HABITACIÓN 1 ---')
    print('')
    print(Fore.GREEN + " En la habitación hay un retrato de una mujer con una vestimenta de otra época.")
    print(Fore.GREEN + " También se pueden ver dos puertas. Una en el oeste y la otra al este.")
    print('')

    opcion = input(Fore.YELLOW + 'mirar cuadro, ir oeste, este o sur?: ')

    if opcion in ['mirar', 'mirar cuadro', 'ver']:
        print('')
        print(Fore.GREEN + " Sus ojos tienen un brillo aterrador, parecieran estar mirándote...")
        print(Fore.GREEN + ' Hay una inscripción debajo en la que puede leerse "Sofia Lumper - 1816".')
        input(Fore.YELLOW + '\nPulsa cualquier tecla para salir...')
        return 'castillo_room1'
    elif opcion == "oeste":
        return 'castillo_room2'
    elif opcion == "este":
        return 'castillo_room3'
    elif opcion == 'sur':
        return 'castillo_entrada'
    elif opcion == 'opciones':
        menus.opciones()
        return 'castillo_room1'
    else:
        print(Fore.RED + '¡Opción no válida!')
        time.sleep(1)
        return 'castillo_room1'

# ROOM 2 --------------------------------------------------------------------------

def room2():
    estado.ubicacion_personaje['posicion'] = 'castillo_room2'
    ia_enemigos.creaEnemigoAleatorio()
    objeto_crucifijo = True # Esto debería estar en el estado global realmente

    funciones.borrarPantalla()
    print(Fore.RED + '--- HABITACIÓN 2 ---')
    print('')
    print(Fore.GREEN + ' Estás en una habitación lúgubre con una puerta al norte, otra al este y una ventana.')
    print(Fore.GREEN + ' Hay un cadáver en el suelo con un crucifijo clavado en el pecho.')
    print('')

    opcion = input(Fore.YELLOW + 'mirar ventana, coger crucifijo, este, norte?: ')

    if 'crucifijo' in opcion:
        funciones.crearObjetoHabilidad('un Crucifijo', 'escudo', 12)
        return 'castillo_room2'
    elif 'ventana' in opcion:
        funciones.borrarPantalla()
        print(Fore.GREEN + ' Se ve un jardín y una mujer pálida que se parece a "Sophia"...')
        opcion_v = input(Fore.YELLOW + '¿Volver o saltar?: ')
        if 'saltar' in opcion_v:
            print(Fore.RED + '\n¡Has caído al vacío!')
            time.sleep(2)
            print(Fore.RED + 'GAME OVER')
            sys.exit()
        return 'castillo_room2'
    elif opcion == 'norte':
        return 'castillo_room4'
    elif opcion == 'este':
        return 'castillo_room1'
    else:
        print(Fore.RED + '¡Opción no válida!')
        time.sleep(1)
        return 'castillo_room2'

# ROOM 3 --------------------------------------------------------------------------


def room3():
    estado.ubicacion_personaje['posicion'] = 'castillo_room3'

    funciones.borrarPantalla()
    print(Fore.RED + '--- HABITACIÓN 3 ---')
    print('')
    print(Fore.GREEN + "Esta habitación es un cristo!")
    direc = input(Fore.YELLOW + "¿oeste? ")
    if direc == "oeste":
        return 'castillo_room1'

# ROOM 4 --------------------------------------------------------------------------


personaje = estado.personaje


def room4():
    estado.ubicacion_personaje['posicion'] = 'castillo_room4'

    funciones.borrarPantalla()

    while True:
        print(Fore.RED + '--- HABITACIÓN 4 ---')
        print('')
        print(Fore.GREEN + "Algo te espera en el norte")

        opcion = input(Fore.YELLOW + "¿ir norte o este? ")

        if opcion == "norte":
            return 'castillo_room2'

        elif opcion == "este":
            return 'castillo_room3'

        else:
            print(Fore.RED + 'Opción no válida!')
            time.sleep(1)
            funciones.borrarPantalla()
            # Quitamos la recursividad aquí también
            return 'castillo_room4'

