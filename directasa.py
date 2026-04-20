import sys
import time
from src import menus, funciones, estado, castillo, pueblo, bosque, cementerio
from colorama import init, Fore, Back, Style

personaje = estado.personaje

init(autoreset=True) 

def game_loop():
    """Bucle principal que gestiona el flujo del juego sin recursividad."""
    proxima_escena = estado.ubicacion_personaje.get('posicion', 'pueblo_plaza')
    
    if not proxima_escena:
        proxima_escena = 'pueblo_plaza'

    while True:
        # Mapeo de nombres de escena a funciones
        escenas = {
            'pueblo_plaza': pueblo.plaza,
            'pueblo_taberna': pueblo.taberna,
            'pueblo_herreria': pueblo.herreria,
            'pueblo_sur': pueblo.pueblo_sur,
            'bosque_entrada': bosque.bosque_entrada,
            'bosque_claro': bosque.claro,
            'bosque_cueva': bosque.cueva,
            'cementerio_entrada': cementerio.entrada_cementerio,
            'cementerio_mausoleo': cementerio.mausoleo,
            'cementerio_capilla': cementerio.capilla,
            'inicio_original': mostrar_introduccion_castillo,
            'castillo_entrada': castillo.entrada,
            'castillo_room1': castillo.room1,
            'castillo_room2': castillo.room2,
        }

        if proxima_escena in escenas:
            resultado = escenas[proxima_escena]()
            if resultado:
                proxima_escena = resultado
        elif proxima_escena == 'fuera_puente':
            print("\nDecides no entrar. El frío de la noche te abraza mientras te alejas...")
            print("GAME OVER")
            break
        else:
            print(f"Error: La escena '{proxima_escena}' no está definida.")
            break

def mostrar_introduccion_castillo():
    """Esta es la escena original del puente, ahora llamada desde el cementerio."""
    funciones.borrarPantalla()
    print('')
    print(" Al fin llegas frente a las puertas del Castillo de Sophia.")
    print(" Una fuerza oscura y demoníaca emana de los muros de piedra.")
    print(" Se escuchan gritos sordos en el interior...")
    print('')
    print(f"¿Quieres cruzar el puente del castillo, {personaje['nombre']}?")
    print('')

    respuesta = input("(si/no/opciones): ").lower()

    if respuesta in ["si", "s"]:
        return 'castillo_entrada'
    elif respuesta in ["no", "n"]:
        return 'fuera_puente'
    elif respuesta == 'opciones':
        menus.opciones()
        return 'inicio_original'
    else:
        print('Opcion no valida!')
        time.sleep(1)
        return 'inicio_original'

def inicio():
    menus.principal()    
    game_loop()

if __name__ == "__main__":
    inicio()
