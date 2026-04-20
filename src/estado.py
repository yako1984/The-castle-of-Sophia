"""
Opción Guardar/Cargar centralizada con los diccionarios.
Este modulo se encarga de manejar todos los diccionarios del juego y estados del juego, puerta abiertas, personaje etc.
Tambíen de guaradar el estado de los diccionarios y de recuperarlos.
Puedes guardar todos los estados guardas_estado('todos') o guardar solo uno de los que hay guardar_estado('personaje')
Las opciones son: bolsa, personaje, ubicacion. 

Ejmeplos para guardar en diccionario:

import estado

estado.personaje['nombre'] = 'pedro' 
estado.personaje['fuerza'] = 10
estado.ubicacion_personaje['posicion'] = 'castillo_room_1'

ejemplo guardar o cargar el estado de los diccionarios:

import estado

estado.guardar_estado(personaje) 

estado.cargar_estado(personaje) 
"""
import os.path as path
import os
import json
from . import funciones, menus
import time
import getpass
#from . import castillo si descomento esta importacion peta, y la necesito para el modulo de la posicion del personaje

dic_estado = {}
personaje = {}
bolsa = {} 
ubicacion_personaje = {}
posicion_puertas = {}

#NUEVA_PARTIDA-------------------------------------------------------------------------

#Aqui guardamos los datos del usuario, inciamos y almacenamos todos los diccioarios a cero.

def partidaNueva():
	
	funciones.borrarPantalla()
	funciones.leer('src/ascii/castillo.dra', 'rojo', False, False)
	
	nombreUsuario = input("¿Como te llamas?: ")
	
	nombrePartida = (nombreUsuario+'Save.json')

	if path.exists('src/saves/'+nombrePartida):
		print('\nYa hay una partida guardada con ese nombre.')
		print('Si es tuya, elige la opción cargar, si no es tuya escoge otro nombre')
		input('\nPulsa una tecla para continuar...')
		menus.principal()		

	else:
		password = getpass.getpass('Escribe tu nueva contraseña: ')
		passwordCmp = getpass.getpass('Repite tu contraseña: ')

		if password == passwordCmp:
			personaje["nombre"] = nombreUsuario  # Caracteristicas del presonaje
			personaje["password"] = password  # Almacena el password del usuario para luego poder cargar la partida
			personaje["vida"] = 5
			personaje["escudo"] = 10
			personaje["fuerza"] = 10

			bolsa['item_1'] = 'vacio'
			bolsa['item_2'] = 'vacio'	#Inventario definido
			bolsa['item_3'] = 'vacio'
			bolsa['item_4'] = 'vacio'

			ubicacion_personaje['posicion'] = '' #Ubicacion del personaje a cero
			
			posicion_puertas['puerta_aguila'] = ''

			guardar_estado('todos')
			
		else:
			print('Las contraseñas no coinciden.')
			partidaNueva()

#GUARDAR_PARTIDA-------------------------------------------------------------------------        

def guardar_estado(opcion):
	# Asegurar que la carpeta de saves existe
	if not path.exists('src/saves'):
		os.makedirs('src/saves')

	if opcion == 'personaje':
		dic_estado['personaje'] = personaje
	
	elif opcion == 'bolsa':
		dic_estado['bolsa'] = bolsa
	
	elif opcion == 'ubicacion':
		dic_estado['ubicacion_personaje'] = ubicacion_personaje
	
	elif opcion == 'todos':
		dic_estado['personaje'] = personaje
		dic_estado['bolsa'] = bolsa
		dic_estado['ubicacion_personaje'] = ubicacion_personaje
		dic_estado['posicion_puertas'] = posicion_puertas
		print('\n¡Partida guardada con éxito! :)')
		time.sleep(1)
	
	nombreUsuario = personaje.get('nombre', 'jugador')
	
	with open('src/saves/'+nombreUsuario+'Save.json', 'w') as file:
		json.dump(dic_estado, file, indent=4)

#CARGAR_PARTIDA-------------------------------------------------------------------------

def cargar_estado():
	nombreUsuario = input("¿Cómo te llamas?: ")
	nombrePartida = (nombreUsuario+'Save.json')
		
	if path.exists('src/saves/'+nombrePartida):
		with open('src/saves/'+nombrePartida) as file:
			datos = json.load(file)

		# Usar update para cargar datos de forma más eficiente
		if 'personaje' in datos: personaje.update(datos['personaje'])
		if 'bolsa' in datos: bolsa.update(datos['bolsa'])
		if 'posicion_puertas' in datos: posicion_puertas.update(datos['posicion_puertas'])
		if 'ubicacion_personaje' in datos: ubicacion_personaje.update(datos['ubicacion_personaje'])

#-----------------FIN DE LA CARGA-------------------------------------------------------

		print('Se encontro una partida con tu nombre!.')
		
		passwordUser = getpass.getpass('Indica tu contraseña: ')
		passwordGuardado = personaje['password']		

		if passwordUser == passwordGuardado:
			print('La contraseña es correcta!.')
			opcionSobreescribirPartida(nombrePartida)
		
		else:
			print('La contraseña no es correcta.')
			cargar_estado() 	

	else:
		print('No hay ninguna partida guardada con ese nombre.')
		time.sleep(2)
		menus.principal()

#BORRAR_PARTIDA-------------------------------------------------------------------------

def borrarPartida(nombrePartida):
	os.remove('src/saves/'+nombrePartida)

#SOBREESCRIBIR_PARTIDA-------------------------------------------------------------------------

def opcionSobreescribirPartida(nombrePartida):
	opcion = input('[1]Continuar partida\n[2]Empezar nueva partida\n> ')
			
	if opcion == '1':
		#ubicacion_personaje['posicion']
		return
	
	elif opcion == '2':
		opcionBorrar = input('Esto borrara todo tu progreso y empezaras de nuevo\nEstas seguro?\n[1]Si\n[2]No\n> ')
		
		if opcionBorrar == '1':
			borrarPartida(nombrePartida)
			partidaNueva()
		
		elif opcionBorrar == '2':
			cargar_estado()
	
		else:
			print('Esa opcion no existe!')
			time.sleep(2)
			menus.principal()


#PRUEBA CARGAR POSICION JUGADOR
'''
def posicion_jugador():

    if estado.ubicacion_personaje['posicion'] == 'castillo_room1':
        castillo.room1()
'''