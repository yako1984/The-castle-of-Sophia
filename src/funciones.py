import os
import time
from . import modulo_bolsa, estado, menus
from colorama import init, Fore, Back, Style

personaje = estado.personaje

#Limpia la pantalla en cualquier sistema operativo------------------------------------------------------------------

def borrarPantalla(): 
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls") 

#Función para crear objetos en las salas, de habilidad--------------------------------------------------------------
#Ejemplo crearObjeto('un cofre', 'vida', 30) opciones: vida, fuerza, escudo.

def crearObjetoHabilidad (objeto, habilidad, puntos):  
	print('') 
	print('Has encontrado',objeto,'!!')      					
	personaje[habilidad] += puntos
	estado.guardar_estado('personaje')
	print('Tu',habilidad,'aumenta en',puntos,'puntos')
	
	printEstado(personaje)


def leer (archivo, color, mecanografiar, parpadeo):   #Abre archivo de texto plano lo almacena en variable y
	if color == 'rojo':						#lo pega en pantalla con el color seleccioando con o sin efecto mecanografía
		color = Fore.RED 					#Ejemplo leer(castillo.txt, verde, True, True) Con True mecanografía, con False solo pinta el texto
	elif color == 'verde':                  #El segundo True es para colorear el fondo de amarilo y hacer efecto parpadeo
		color = Fore.GREEN
	elif color == 'negro':
		color = Fore.BLACK
	elif color == 'amarillo':
		color = Fore.YELLOW
	elif color == 'azul':
		color = Fore.BLUE
	elif color == 'magenta':
		color = Fore.MAGENTA
	elif color == 'cian':
		color = Fore.CYAN
	elif color == 'blanco':
		color = Fore.WHITE

	f = open (archivo,'r', encoding="utf8")
	mensaje = f.read()
	f.close()

	if mecanografiar == True:
		
		for letra in mensaje:
			print (color+letra, end="", flush=True)
			time.sleep(0.001)

	if parpadeo == True:

		for i in range(5):
			#print(color + mensaje)
			time.sleep(0.05)
			borrarPantalla()
			print(Back.YELLOW + color + mensaje)
			time.sleep(0.05)
			borrarPantalla()
		
	print(color + mensaje)

#IMPRIME EL ESTADO DEL PERSONAJE VIDA, ESCUDO ETC.-----------------------------------------------------			

def printEstado (atributos_personaje):
	print('')
	print(atributos_personaje['nombre'],' - ',"Vida:",atributos_personaje["vida"],"Escudo:",atributos_personaje["escudo"],"Fuerza:",atributos_personaje["fuerza"])
	print('')
	input('\nPulsa cualquier tecla par cotinua...')

#Comprueba si tienes la llave en la bolsa (inventario). Si la tienes abre la puerta--------------------------------
#------------------------------------------------------------------------------------------------------------------
#EJEMPLO FUNCIONAMIENTO:

#funciones.abrir_puerta('puerta_aguila', 'llave_aguila')
	#if estado.posicion_puertas['puerta_aguila'] == 'abierta':
            #funciones.puntosCardinales(opcion, 'norteSi', room1, 'surNo', room2, 'esteNo', 0, 'oesteNo', 0)
#------------------------------------------------------------------------------------------------------------------
def abrir_puerta(puerta, llave):
	bolsa = modulo_bolsa.bolsa.values()		#Ejemplo abrir_puerta('nombre_puerta', 'nombre_llave')
	
	if estado.posicion_puertas[puerta] == 'abierta':
		return
	else:
		for i in bolsa:
			if i == llave:
				print('\nLa puerta se abrió...')
				estado.posicion_puertas[puerta] = 'abierta'
				modulo_bolsa.eliminar_bolsa(llave)
				input()
				return
	
		print('La ' +puerta+ ' esta cerrada con ' +llave)
		input()

#Mecanografia un testo y le da un color ejemp: mecanografiar('Hola que tal estas', 'verde') REVISAR

def mecanografiar(color, texto):
	if color == 'rojo':						
		color = Fore.RED 					
	elif color == 'verde':                  
		color = Fore.GREEN
	elif color == 'negro':
		color = Fore.BLACK
	elif color == 'amarillo':
		color = Fore.YELLOW
	elif color == 'azul':
		color = Fore.BLUE
	elif color == 'magenta':
		color = Fore.MAGENTA
	elif color == 'cian':
		color = Fore.CYAN
	elif color == 'blanco':
		color = Fore.WHITE

	for letra in texto:
		print (color + letra, end="", flush=True)
		#print (letra, end="", flush=True)
		time.sleep(0.03)

#FUNCION PUNTOS CARDINALES---------------------------------------------------------------------------

def puntosCardinales(respuesta, opcionNorte, roomNorte, opcionSur, roomSur, opcionEste, roomEste, opcionOeste, roomOeste):
	
	frase = respuesta.split() # Separa la frase(trocea) por palabras.

	for palabra in frase:

		if palabra == 'no':
			print('No lo hagas nadie te obliga!!')
			time.sleep(2)
			return
		
		elif  palabra == 'norte' and opcionNorte == 'norteSi':
			roomNorte()
			
		elif palabra == 'norte' and opcionNorte == 'norteNo': 
			print('No puedes ir por el norte!')
			time.sleep(2)		
			return

		elif palabra == 'sur' and opcionSur == 'surSi': 
			roomSur()

		elif palabra == 'sur' and opcionSur == 'surNo': 
			print('No puedes ir al sur!')
			time.sleep(2)
			return
		elif palabra == 'este' and opcionEste == 'esteSi': 
			roomEste()

		elif palabra == 'este' and opcionEste == 'esteNo': 
			print('No puedes ir al este!')
			time.sleep(2)
			return
		
		elif palabra == 'oeste' and opcionOeste == 'oesteSi': 
			roomOeste()

		elif palabra == 'oeste' and opcionOeste == 'oesteNo': 
			print('No puedes ir al oeste!')
			time.sleep(2)
			return
		
		elif palabra == 'opciones':
			menus.opciones()
	
	print('\nNo entiendo lo que dices!')
	time.sleep(2)
			

#la funcion sin los parentesis () se pasa como un parametro pero no llamas a la funcion
#para llamar a la funcion tienes que poner () 
#las funciones se pueden pasar sin los () y asignarlas a una variable
#y llamarla despues poniendo delante de la varible aisgnada ()

'''
Ejemplo:
	respuesta = input('que quieres hacer aqui ahora?: ')
	
	puntosCardinales(respuesta, 'norteNo', '0', 'surSi', room2)
'''