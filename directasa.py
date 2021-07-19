import sys
import time
from src import menus
from src import funciones
from src import estado
from src import castillo
from colorama import init, Fore, Back, Style

personaje = estado.personaje

init(autoreset=True) #Inicializador colorama - Atencion: Para usar colorama hay que poner esta linea al inicio!


# FUNCIONES AÑADIDAS ###################   Notas: Hacer funcion GAME OVER, para que se pueda volver a empezar o continuar

def posicion_jugador():

    if estado.ubicacion_personaje['posicion'] == 'castillo_room1':
        castillo.room1()

############ FUNCIONES AÑADIDAS ###################

def Molyneux():
    funciones.borrarPantalla()

    vida_enemigo = 50
    fuerza_enemigo = 20

    print("Hola! Soy Moli... Muli... Mo... El tito Peter!")
    print("Me vas a permitir matarte...")
    print("¡Tiene", vida_enemigo, "puntos de vida!")
    while vida_enemigo > 0:
        print("")
        accion = input("atacar o escapar: ")
        if accion == "atacar":
            vida_enemigo = vida_enemigo - personaje["fuerza"]
            if vida_enemigo <= 0:
                print("Ganaste!!! el final ya esta aqui!!!")
                time.sleep(5)
                funciones.borrarPantalla()
                #TheEnd()
                return False
            else:
                print("A Peter le quedan", vida_enemigo, "puntos de vida")
                print("La Peter ataca!!!!")
                if personaje["escudo"] <= 0:
                    personaje["vida"] -= fuerza_enemigo
                    if personaje["vida"] <= 0:
                        print("GAME OVER")
                        sys.exit()
                else:
                    personaje["escudo"] -= fuerza_enemigo

            funciones.printEstado(personaje)

        elif accion != "atacar" or accion != "escapar":
            print('Opcion incorrecta! ')

        else:
            print("Escapaste")
            return False

    return

def inicio():
    menus.principal()    
    
    posicion_jugador()
    
# PUENTE CASTILLO -------------------------------------------------------------------------------------------------
    
    while True:

        print('')
        print(" Algo te atrajo hasta aqui. Una fuerza oscura y demoniaca.")
        print(" En frente a ti se alza un castillo con una gran puerta de madera, que data de 1800.")
        print(" Se escuchan gritos sordos...")
        print(" Ser cobarde no es una opción")
        print('')
        print("¿Quieres cruzar el puente del castillo", personaje["nombre"], "?")
        print('')

        respuesta = input("(si/no): ")

        if respuesta == "si":
            castillo.entrada()

        elif respuesta == 'no':
            funciones.borrarPantalla()
            print(" Puede que sea una buena idea.")
            print(" LIMPIATE EL CULO!!")
            print('')
            print(" GAME OVER")
            time.sleep(4)
            sys.exit()

        elif respuesta == 'opciones':
            menus.opciones()

        else:
            print('Opcion no valida!')
            time.sleep(1)

###################### Inicio ####################################


inicio()
