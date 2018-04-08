#!/usr/bin/env python
'''
Creado el 08.04.2018

@author: Maximiliano R Soria
@version: 1.0 
@note: Creado para la catedra de Programacion en tiempo real.

'''

#Una class se un 'Plano' o una representacion de un algo que posee metodos y atributos
#Atrubuto - Caracteristica de una clase
#Metodo - Funcion que ejecuta comportamiento de la clase
#Objeto - Clase Instanciada
#Constructor - Metodo especial que marca con que valores se inicializa la clase

#Clase Persona
class Persona():
	#Constructor  -> Valores por defecto (self, nombre="test1", apellido="test1", dni=0) 
	def __init__(self, nombre="test1", apellido="test1", dni=0):
		#Atributos
		self._nombre = nombre
		self._apellido = apellido
		self._dni = dni
	
	
	#Metodo ObtenerDatos() 	
	def obtenerDatos(self):
		print("\nEl nombre es: ")
		print(self._nombre)  
		print("\nEl apellido es: ")
		print(self._apellido) 
		print("\nEl dni es: ")
		print(self._dni) 
		
	


def main():	
	#Objeto, lleando el constructor
	persona = Persona("Maxi", "Soria", 33089610)
	persona.obtenerDatos()
	
	#Objeto2, constructor con valores por defecto
	persona2 = Persona()
	persona2.obtenerDatos();
main()
