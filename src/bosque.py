import time
import random
from colorama import Fore, Style
from . import funciones, estado, ia_enemigos

def bosque_entrada():
    estado.ubicacion_personaje['posicion'] = 'bosque_entrada'
    funciones.borrarPantalla()
    funciones.leer('src/ascii/bosque.dra', 'verde', False, False)
    
    print(Fore.GREEN + Style.BRIGHT + "\n==========================================")
    print("        EL BOSQUE DE LAS SOMBRAS         ")
    print("==========================================" + Style.RESET_ALL)
    
    print(Fore.GREEN + "\nLos árboles son tan altos que ocultan la luna. Sus ramas parecen dedos")
    print("esqueléticos que intentan atraparte. El aire es denso y huele a tierra húmeda.")
    
    print(Fore.CYAN + "\nSENDEROS DISPONIBLES:")
    print("---------------------")
    print("Al NORTE: El camino principal hacia el CEMENTERIO.")
    print("Al ESTE: Un CLARO donde la luz de la luna logra filtrarse.")
    print("Al OESTE: Una CUEVA OSCURA de la que emana un frío glacial.")
    print("Al SUR: Regresar a la seguridad de la PLAZA del pueblo.")
    
    print(Style.DIM + "\n(Escribe: norte, este, oeste, sur u opciones)")
    
    opcion = input(Fore.YELLOW + "\n¿Qué sendero eliges?: " + Style.RESET_ALL).lower()

    if 'norte' in opcion:
        print(Fore.RED + "\nTe adentras en lo profundo del bosque...")
        time.sleep(1)
        # Probabilidad de encuentro aleatorio
        if random.randint(1, 100) > 60:
            ia_enemigos.creaEnemigoAleatorio()
        return 'cementerio_entrada'
    elif 'este' in opcion:
        return 'bosque_claro'
    elif 'oeste' in opcion:
        return 'bosque_cueva'
    elif 'sur' in opcion:
        return 'pueblo_plaza'
    elif 'opciones' in opcion:
        from . import menus
        menus.opciones()
        return 'bosque_entrada'
    else:
        print(Fore.RED + "\nTe pierdes entre los árboles un momento, confundido por los susurros...")
        time.sleep(1.5)
        return 'bosque_entrada'

def claro():
    funciones.borrarPantalla()
    print(Fore.GREEN + Style.BRIGHT + "\n--- EL CLARO EÉREO ---")
    print(Fore.WHITE + "\nUn espacio circular donde la hierba brilla con una luz plateada.")
    print("En el centro, hay un pequeño estanque de aguas cristalinas.")
    
    print(Fore.YELLOW + "\n1. Beber del estanque.")
    print("2. Descansar un momento bajo la luz de la luna.")
    print("3. Examinar el ÁRBOL DE LOS LAMENTOS que se ve al fondo.")
    print("4. Volver a la entrada del bosque.")
    
    opcion = input(Fore.YELLOW + "\n¿Qué deseas hacer?: " + Style.RESET_ALL)
    
    if opcion == '1':
        print(Fore.CYAN + "\nEl agua es pura y refrescante. Sientes cómo tus heridas sanan.")
        print(Fore.MAGENTA + Style.BRIGHT + "[Tu VIDA ha aumentado en +3]")
        estado.personaje['vida'] += 3
        input(Fore.YELLOW + "\nPresiona Enter...")
        return 'bosque_claro'
    elif opcion == '2':
        print(Fore.CYAN + "\nLa paz del lugar templa tus nervios.")
        print(Fore.MAGENTA + Style.BRIGHT + "[Tu ESCUDO ha aumentado en +2]")
        estado.personaje['escudo'] += 2
        input(Fore.YELLOW + "\nPresiona Enter...")
        return 'bosque_claro'
    elif opcion == '3':
        return arbol_lamentos()
    else:
        return 'bosque_entrada'

def cueva():
    funciones.borrarPantalla()
    print(Fore.RED + Style.BRIGHT + "\n--- LA CUEVA OSCURA ---")
    print(Fore.BLACK + Back.WHITE + "\nLa oscuridad aquí es casi tangible. Un hedor a muerte sale de las profundidades.")
    
    print(Fore.YELLOW + "\n¿Te atreves a explorar el interior? (si/no)")
    opcion = input(Fore.RED + "> " + Style.RESET_ALL).lower()
    
    if 'si' in opcion:
        print(Fore.RED + "\nAlgo salta desde las sombras!")
        time.sleep(1)
        ia_enemigos.creaEnemigoAleatorio()
        
        print(Fore.CYAN + "\nTras el combate, encuentras unos viejos guanteletes de hierro.")
        print(Fore.MAGENTA + Style.BRIGHT + "[Tu FUERZA ha aumentado en +3]")
        estado.personaje['fuerza'] += 3
        input(Fore.YELLOW + "\nPresiona Enter para salir de la cueva...")
    
    return 'bosque_entrada'

def arbol_lamentos():
    funciones.borrarPantalla()
    print(Fore.RED + Style.BRIGHT + "\n--- EL ÁRBOL DE LOS LAMENTOS ---")
    print(Fore.GREEN + "\nUn árbol milenario cuyas ramas parecen rostros gritando de dolor.")
    print("Se dice que las almas perdidas en el bosque quedan atrapadas aquí.")
    
    print(Fore.YELLOW + '\nUna voz susurra en tu mente: "Dale algo de valor y te daré mi fuerza..."')
    
    print(Fore.CYAN + "\n¿Ofrecer una parte de tu energía vital? (pierdes 2 VIDA a cambio de 4 FUERZA) (si/no)")
    opcion = input("> ").lower()
    
    if 'si' in opcion:
        if estado.personaje['vida'] > 2:
            print(Fore.MAGENTA + "\nEl árbol absorbe tu sangre y sus ramas se vuelven de un color rojo vibrante.")
            estado.personaje['vida'] -= 2
            estado.personaje['fuerza'] += 4
            print(Style.BRIGHT + "[VIDA -2, FUERZA +4]")
        else:
            print(Fore.RED + "\nEstás demasiado débil para el sacrificio...")
    else:
        print(Fore.GREEN + "\nDecides alejarte del árbol. Sus lamentos parecen intensificarse.")
    
    input(Fore.YELLOW + "\nPresiona Enter para volver al claro...")
    return 'bosque_claro'
