import time
from colorama import Fore, Style
from . import funciones, estado, ia_enemigos

def entrada_cementerio():
    estado.ubicacion_personaje['posicion'] = 'cementerio_entrada'
    funciones.borrarPantalla()
    funciones.leer('src/ascii/cementerio.dra', 'cian', False, False)
    
    print(Fore.CYAN + Style.BRIGHT + "\n==========================================")
    print("       CEMENTERIO DE LOS OLVIDADOS       ")
    print("==========================================" + Style.RESET_ALL)
    
    print(Fore.CYAN + "\nLlegas a una verja de hierro oxidada. Tras ella, cientos de tumbas")
    print("blancas brillan bajo la niebla. El castillo de Sophia se alza")
    print("majestuoso e imponente justo al NORTE.")
    
    print(Fore.WHITE + "\nLUGARES DE INTERÉS:")
    print("-------------------")
    print("Al NORTE: El puente levadizo del CASTILLO.")
    print("Al ESTE: El MAUSOLEO de la familia Sophia.")
    print("Al OESTE: Una CAPILLA EN RUINAS.")
    print("Al SUR: Regresar al BOSQUE de las Sombras.")
    
    print(Style.DIM + "\n(Escribe: norte, este, oeste, sur u opciones)")
    
    opcion = input(Fore.YELLOW + "\n¿Hacia dónde te diriges?: " + Style.RESET_ALL).lower()

    if 'norte' in opcion:
        print(Fore.CYAN + "\nCruzas el cementerio. Las lápidas parecen susurrar tu nombre...")
        time.sleep(2)
        return 'inicio_original' # El puente del castillo
    elif 'este' in opcion:
        return 'cementerio_mausoleo'
    elif 'oeste' in opcion:
        return 'cementerio_capilla'
    elif 'sur' in opcion:
        return 'bosque_entrada'
    elif 'opciones' in opcion:
        from . import menus
        menus.opciones()
        return 'cementerio_entrada'
    else:
        print(Fore.RED + "\nEl frío del cementerio te paraliza los huesos...")
        time.sleep(1.5)
        return 'cementerio_entrada'

def mausoleo():
    funciones.borrarPantalla()
    print(Fore.CYAN + Style.BRIGHT + "\n--- EL MAUSOLEO DE LOS SOPHIA ---")
    print(Fore.WHITE + "\nUna imponente estructura de mármol negro. La puerta está entreabierta.")
    print("En el interior, el aire es gélido y huele a incienso antiguo.")
    
    print(Fore.YELLOW + "\n1. Buscar entre los sarcófagos.")
    print("2. Leer las inscripciones de las paredes.")
    print("3. Volver a la entrada.")
    
    opcion = input(Fore.YELLOW + "\n¿Qué decides?: " + Style.RESET_ALL)
    
    if opcion == '1':
        print(Fore.RED + "\n¡Al mover una pesada losa, despiertas a un Guardián!")
        time.sleep(1)
        ia_enemigos.creaEnemigoAleatorio()
        print(Fore.CYAN + "\nEn el interior del sarcófago encuentras una reliquia.")
        print(Fore.MAGENTA + Style.BRIGHT + "[Tu FUERZA ha aumentado en +3]")
        estado.personaje['fuerza'] += 3
        input(Fore.YELLOW + "\nPresiona Enter...")
        return 'cementerio_mausoleo'
    elif opcion == '2':
        print(Fore.GREEN + "\nLas inscripciones hablan de una tal Sophia y su pacto con la oscuridad.")
        print(Fore.YELLOW + '"El corazón del castillo late con la sangre de los inocentes..."')
        input(Fore.YELLOW + "\nPresiona Enter para continuar...")
        return 'cementerio_mausoleo'
    else:
        return 'cementerio_entrada'

def capilla():
    funciones.borrarPantalla()
    print(Fore.CYAN + Style.BRIGHT + "\n--- LA CAPILLA EN RUINAS ---")
    print(Fore.WHITE + "\nEl techo se ha derrumbado, pero un altar permanece intacto.")
    print("Un rayo de luz lunar cae directamente sobre una cruz de piedra.")
    
    print(Fore.YELLOW + "\n1. Rezar en el altar.")
    print("2. Buscar en la CRIPTA que hay bajo el altar.")
    print("3. Volver a la entrada.")
    
    opcion = input(Fore.YELLOW + "\n¿Qué decides?: " + Style.RESET_ALL)
    
    if opcion == '1':
        print(Fore.CYAN + "\nSientes una calidez divina recorriendo tu cuerpo.")
        print(Fore.MAGENTA + Style.BRIGHT + "[Has recuperado toda tu VIDA y ESCUDO]")
        estado.personaje['vida'] = 10 # Asumiendo un máximo o simplemente dando mucho
        estado.personaje['escudo'] += 5
        input(Fore.YELLOW + "\nPresiona Enter...")
        return 'cementerio_capilla'
    elif opcion == '2':
        return cripta()
    else:
        return 'cementerio_entrada'

def cripta():
    funciones.borrarPantalla()
    print(Fore.RED + Style.BRIGHT + "\n--- LA CRIPTA BAJO EL ALTAR ---")
    print(Fore.BLACK + Back.WHITE + "\nEs un lugar estrecho y claustrofóbico. Hay huesos por todas partes.")
    
    print(Fore.YELLOW + "\nEncuentras un viejo escudo de caballero entre los restos.")
    print(Fore.MAGENTA + Style.BRIGHT + "[Tu ESCUDO ha aumentado en +10]")
    estado.personaje['escudo'] += 10
    
    input(Fore.YELLOW + "\nPresiona Enter para salir de la cripta...")
    return 'cementerio_capilla'
