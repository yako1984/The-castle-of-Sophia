import time
from colorama import init, Fore, Back, Style
from . import estado
from . import funciones
from . import menus

bolsa = estado.bolsa

#Función Elilminar item ---------------------------------------------------- 

def eliminar_bolsa(objeto):
		
		for i, o in bolsa.items():
			if objeto == o:
				bolsa[i] = 'vacio'
				print(objeto, Fore.RED + 'Eliminado...')
				time.sleep(2)
				
				return

		print(Fore.RED + 'Ese objeto no lo tienes en el inventario!')

		time.sleep(2)

# Función para añadir item ---------------------------------------------------

def añadir_bolsa(objeto): 
	
	for i, o in bolsa.items():
		if o == 'vacio':
			print('Has cogido',objeto,'!!')
			bolsa[i] = objeto
			
			return 

	print('Tu bolsa esta llena, no puedes coger el objeto.\nPuedes entrar en "opciones" y borrar un objeto que ya no necesites.')

#Funcion bolsa ----------------------------------------------------------------------------

def ver_bolsa():	
	
	while True:		
		
		funciones.borrarPantalla()

		print (Fore.RED + '\n+--------+ INVENTARIO +--------+')
				
		for i, o in bolsa.items():
			print('   ', Fore.GREEN + i, ':', Fore.MAGENTA + o)
		
		print(Fore.RED + '+------------------------------+')

		print(Fore.YELLOW + '[1]Eliminar objeto\n[2]Salir')
		opcion = input(Fore.YELLOW + '\nOpción: ')
		
		if opcion == '1':
			obj_eliminar = input(Fore.YELLOW + 'Escribe el nombre del objeto que quieres eliminar?: ')
			eliminar_bolsa(obj_eliminar)

		elif opcion == '2':
			menus.opciones() 

		else:
			print(Fore.RED + 'Esa opción no es válida.')
			time.sleep(2)
