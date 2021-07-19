import time
from colorama import init, Fore, Back, Style
from . import funciones
from . import estado
from . import modulo_bolsa

def principal():

    funciones.borrarPantalla()
    funciones.leer('src/ascii/castillo.dra', 'rojo', False, False)

    print(Fore.RED + '+--------+ MENU PRINCIPAL +--------+')
    print(Fore.GREEN + '[1] Partida nueva')
    print(Fore.GREEN + '[2] Cargar partida')
    print(Fore.GREEN + '[3] Instrucciones del juego')
    print(Fore.GREEN + '[4] Salir')	
    print(Fore.RED +'+-----------------------------------+')
    
    opcion_usuario = input (Fore.YELLOW + 'Opción: ')

    if opcion_usuario == '1':
        estado.partidaNueva()
    
    elif opcion_usuario == '2':
        estado.cargar_estado()
    
    elif opcion_usuario == '3':
        print('Este manual de ayuda e instruccciones aun esta en desarrollo.')
        time.sleep(2)
        principal()

    elif opcion_usuario == '4':
        opcion = input('Estas segura que quieres salir del juego?\n Si/No: ')
        
        if opcion in ['SI','Si','si','S','s','yes']:
            exit()
        else:
            principal()
        
    else:
        print ('Esa opción no es valida.')
        time.sleep(2)
        principal()
            

def opciones():
	
	funciones.borrarPantalla()

	print(Fore.RED + '+--------+ MENU OPCIONES +----------+')
	print(Fore.GREEN + '[1] Ver y/o editar el inventario')
	print(Fore.GREEN + '[2] Guardar la partida')
	print(Fore.GREEN + '[3] Ver el estado del personaje')
	print(Fore.GREEN + '[4] Salir')	
	print(Fore.RED +'+-----------------------------------+')
	
	opcion_personaje = input (Fore.YELLOW + 'Opción: ')

	if opcion_personaje == '1':
		modulo_bolsa.ver_bolsa()
	
	elif opcion_personaje == '2':
		estado.guardar_estado('todos')
	
	elif opcion_personaje == '3':
		funciones.printEstado(estado.personaje)

	elif opcion_personaje == '4':
		return
		
	else:
		print ('Esa opción no esta registrada.')
		time.sleep(0.500)
		opciones()