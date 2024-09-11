import random
import time
import sys
from . import funciones, estado, ia_enemigos

# ENTRADA --------------------------------------------------------------------------
def entrada():
    while True:
        estado.ubicacion_personaje['posicion'] = 'castillo_entrada'

        funciones.borrarPantalla()
        #funciones.leer('src/ascii/lobo.dra', 'azul', True, True)

        print('Entrada')
        print('')
        print(" Una niebla intensa dificulta la visibilidad.")
        print(" Hay una gran puerta de madera al norte")
        print(" Al sur vuelves a cruzar el puente")
        print('')

        opcion = input("¿norte o sur? ")
        
        
        if opcion == 'norte': 
            funciones.puntosCardinales(opcion, 'norteSi', room1, 'surNo', room2, 'esteNo', 0, 'oesteNo', 0)
    
        else:
            funciones.puntosCardinales(opcion, 'norteNo', room1, 'surNo', room2, 'esteNo', 0, 'oesteNo', 0)
        

# ROOM 1 --------------------------------------------------------------------------


def room1():
    estado.ubicacion_personaje['posicion'] = 'castillo_room1' 

    while True:
        funciones.borrarPantalla()
        print('Habitación 1')
        print('')
        print(" En la habitación hay un retrato de una mujer con una vestimenta de otra epoca.")
        print(" Tambien se pueden ver dos puertas. Una en el oeste y la otra al este")
        print('')

        opcion = input('mirar cuadro, ir oeste, este o sur?: ')

        if opcion == 'mirar' or opcion == 'mirar cuadro' or opcion == 'ver':
            print('')
            print(" Sus ojos tienen un brillo aterrador, parecieran estar mirandote...")
            print(
                ' Hay una inscripción debajo en la que puede leerse "Sofia Lumper - 1816".')
            input('\npulsa cualquier tecla para salir...')
        elif opcion == "oeste":
            room2()
        elif opcion == "este":
            room3()
        elif opcion == 'sur':
            entrada()
        elif opcion == 'opciones':
            funciones.opciones()
        else:
            print('Opción no válida!')
            time.sleep(1)

# ROOM 2 --------------------------------------------------------------------------


def room2():
    estado.ubicacion_personaje['posicion'] = 'castillo_room2'

    ia_enemigos.creaEnemigoAleatorio()
    objeto = True

    while True:
        funciones.borrarPantalla()
        print('Habitación 2')
        print('')
        print(' Estas en una habitacion lugrube en la que se puede ver una puerta al norte, otra al este y una ventana.')
        print(' También hay un cadaver en suelo desnudo, tiene un crucifijo clavado en el pecho.')
        print(' El crucifijo puede verse destellando en la habitación')
        print('')

        opcion = input('mirar ventana, coger crucifijo, este, norte?: ')

        if opcion == 'coger crucifijo' or opcion == 'coger el crucifijo':
            if objeto == True:
                funciones.crearObjetoHabilidad('un Crucifijo', 'escudo', 12)
                objeto = False

            elif objeto == False:
                print('Ya tines el crucifijo!')
                time.sleep(1)

        elif opcion == 'mirar ventana' or opcion == 'mirar la ventana':

            while True:  # Mirar Ventana
                funciones.borrarPantalla()
                print(
                    ' Se ve un jardin, y en medio una mujer de aspecto palido. Tiene un cierto parecido al retrato de "Sophia"...')
                print('')

                opcion = input(
                    'Que quieres hacer: volver o saltar por la ventana?: ')

                if opcion == 'saltar por la ventana' or opcion == 'saltar ventana' or opcion == 'saltar':
                    print('')
                    print('Has caido al vacio!!')
                    time.sleep(2)
                    print('La mujer se hacerca a ti. La vision se vuelve borrosa')
                    time.sleep(2)
                    print('Ya no puedes pensar nada mas que en sangre...')
                    time.sleep(2)
                    print('')
                    print('GAME OVER')
                    sys.exit()
                elif opcion == 'volver' or opcion == 'atras':
                    room2()

                else:
                    print('Opción no válida!')
                    time.sleep(1)

        elif opcion == 'norte':
            room4()
        elif opcion == 'este':
            room1()
        else:
            print('Opción no válida!')
            time.sleep(1)

# ROOM 3 --------------------------------------------------------------------------


def room3():
    estado.ubicacion_personaje['posicion'] = 'castillo_room3'

    funciones.borrarPantalla()
    print('Habitación 3')
    print('')
    print("Esta habitación es un cristo!")
    direc = input("¿oeste? ")
    if direc == "oeste":
        room1()

# ROOM 4 --------------------------------------------------------------------------


personaje = estado.personaje


def room4():
    estado.ubicacion_personaje['posicion'] = 'castillo_room4'

    funciones.borrarPantalla()

    while True:
        print('Habitación 4')
        print('')
        print("Algo te espera en el norte")

        opcion = input("¿ir norte o este? ")

        if opcion == "norte":
            room2()

        elif opcion == "este":
            room3()

        else:
            print('Opción no válida!')
            time.sleep(1)
            funciones.borrarPantalla()
            room4()

