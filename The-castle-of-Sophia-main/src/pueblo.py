import time
from colorama import Fore, Style
from . import funciones, estado, modulo_bolsa

def plaza():
    estado.ubicacion_personaje['posicion'] = 'pueblo_plaza'
    funciones.borrarPantalla()
    funciones.leer('src/ascii/pueblo.dra', 'blanco', False, False)
    
    print(Fore.RED + Style.BRIGHT + "\n==========================================")
    print("       LA PLAZA CENTRAL DE VALAKIA       ")
    print("==========================================" + Style.RESET_ALL)
    
    print(Fore.GREEN + "\nTe encuentras en el corazón del pueblo. El silencio es opresivo.")
    print("La niebla se arrastra por el suelo empedrado, ocultando los pies de")
    print("las estatuas decapitadas que adornan la plaza.")
    
    print(Fore.CYAN + "\nLUGARES CERCANOS:")
    print("-----------------")
    print("Al NORTE: El sendero hacia el BOSQUE oscuro.")
    print("Al ESTE: El brillo tenue de la TABERNA del Cojo.")
    print("Al OESTE: El humo negro de la HERRERÍA.")
    print("Al SUR: Un viejo POZO y una CASA DERRUIDA.")
    
    print(Style.DIM + "\n(Escribe: norte, este, oeste, sur u opciones)")
    
    opcion = input(Fore.YELLOW + "\n¿Hacia dónde se dirigen tus pasos?: " + Style.RESET_ALL).lower()

    if 'norte' in opcion:
        return 'bosque_entrada'
    elif 'este' in opcion:
        return 'pueblo_taberna'
    elif 'oeste' in opcion:
        return 'pueblo_herreria'
    elif 'sur' in opcion:
        return 'pueblo_sur'
    elif 'opciones' in opcion:
        from . import menus
        menus.opciones()
        return 'pueblo_plaza'
    else:
        print(Fore.RED + "\nCaminas sin rumbo, sintiendo ojos que te observan tras las cortinas...")
        time.sleep(1.5)
        return 'pueblo_plaza'

def pueblo_sur():
    funciones.borrarPantalla()
    print(Fore.RED + Style.BRIGHT + "\n--- CALLEJÓN DEL OLVIDO ---")
    print(Fore.GREEN + "\nAquí el pueblo parece morir. El viento silba entre las ruinas.")
    print("\n1. Inspeccionar el POZO ABANDONADO.")
    print("2. Explorar la CASA DERRUIDA.")
    print("3. Volver a la PLAZA.")
    
    opcion = input(Fore.YELLOW + "\n¿Qué deseas hacer?: " + Style.RESET_ALL)
    
    if opcion == '1':
        return pozo()
    elif opcion == '2':
        return casa_derruida()
    else:
        return 'pueblo_plaza'

def taberna():
    funciones.borrarPantalla()
    print(Fore.RED + Style.BRIGHT + "\n--- LA TABERNA DEL COJO ---")
    print(Fore.GREEN + "\nUn lugar maloliente pero cálido. Un viejo te observa desde una esquina.")
    print("El aire está cargado de humo de pipa y olor a cerveza agria.")
    
    if 'Amuleto de Ajo' not in str(estado.bolsa.values()):
        print(Fore.GREEN + "\nEl viejo se acerca y te dice con voz temblorosa:")
        print(Fore.YELLOW + '"¿Vas al castillo de Sophia? Muchos han ido, pero solo el viento ha vuelto..."')
        print(Fore.YELLOW + '"Lleva este amuleto de ajo, quizá te salve el cuello."')
        
        print(Fore.MAGENTA + Style.BRIGHT + "\n[HAS RECIBIDO: Amuleto de Ajo (Fuerza +2)]")
        estado.personaje['fuerza'] += 2
        modulo_bolsa.añadir_bolsa('Amuleto de Ajo')
    else:
        print(Fore.YELLOW + '\n"Ya tienes el amuleto, forastero. No tientes a la suerte..."')
        print("El viejo vuelve a sus sombras y sigue bebiendo en silencio.")

    input(Fore.YELLOW + "\nPresiona Enter para volver a la plaza...")
    return 'pueblo_plaza'

def herreria():
    funciones.borrarPantalla()
    print(Fore.RED + Style.BRIGHT + "\n--- LA HERRERÍA DE BROKK ---")
    print(Fore.GREEN + "\nEl calor de la forja es lo único que parece vivo en este pueblo.")
    print("Un hombre corpulento golpea un metal al rojo vivo sobre el yunque.")
    
    print(Fore.YELLOW + '\n"Si buscas hierro para el castillo, has venido al lugar correcto,"')
    print('"pero la calidad tiene un precio en sangre y sudor."')
    
    print(Fore.CYAN + "\nEl herrero refuerza tu equipo gratuitamente esta vez.")
    print(Fore.MAGENTA + Style.BRIGHT + "[Tu ESCUDO ha aumentado en +5]")
    estado.personaje['escudo'] += 5
    
    input(Fore.YELLOW + "\nPresiona Enter para volver a la plaza...")
    return 'pueblo_plaza'

def pozo():
    funciones.borrarPantalla()
    print(Fore.RED + Style.BRIGHT + "\n--- EL POZO ABANDONADO ---")
    print(Fore.GREEN + "\nUn pozo antiguo cubierto de musgo. El agua en el fondo está estancada.")
    print("Arrojas una piedra y tarda mucho en sonar el impacto...")
    
    print(Fore.YELLOW + "\nDecides buscar algo de valor entre las grietas de las piedras.")
    
    import random
    suerte = random.randint(1, 3)
    
    if suerte == 1:
        print(Fore.CYAN + "\n¡Has encontrado una Moneda Antigua incrustada en el muro!")
        print(Fore.MAGENTA + "[Fuerza +1 por el esfuerzo]")
        estado.personaje['fuerza'] += 1
    elif suerte == 2:
        print(Fore.RED + "\nUna rata te muerde mientras buscabas.")
        print(Fore.MAGENTA + "[Pierdes 1 punto de VIDA]")
        estado.personaje['vida'] -= 1
    else:
        print(Fore.GREEN + "\nNo encuentras nada más que humedad y oscuridad.")
    
    input(Fore.YELLOW + "\nPresiona Enter para volver...")
    return 'pueblo_sur'

def casa_derruida():
    funciones.borrarPantalla()
    print(Fore.RED + Style.BRIGHT + "\n--- LA CASA DERRUIDA ---")
    print(Fore.GREEN + "\nLas vigas de madera están podridas y el techo se ha hundido.")
    print("En una de las paredes, hay un mensaje escrito con algo rojo:")
    print(Fore.RED + '\n"ELLA NOS ESPERA EN EL CASTILLO..."')
    
    print(Fore.GREEN + "\nEncuentras unos restos de comida enlatada que parecen comestibles.")
    print(Fore.MAGENTA + Style.BRIGHT + "[Tu VIDA ha aumentado en +2]")
    estado.personaje['vida'] += 2
    
    input(Fore.YELLOW + "\nPresiona Enter para volver...")
    return 'pueblo_sur'
