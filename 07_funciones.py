#!/usr/bin/env python
'''
Creado el 08.04.2018

@author: Maximiliano R Soria
@version: 1.0 
@note: Creado para la catedra de Programacion en tiempo real.

'''

#Funcion - Es una es la referencia a porcion de codigo 

#Sumar espera dos parametros 'a' y 'b' y retorna su suma. 
def sumar(a,b):
	return a + b
	
#'mensaje()' muestra por pantalla un mensaje
def mensaje():
	print("\nEste es el resultado:")	
	
	
#La funcion 'main()' utiliza como funcion principal, la que contendra el flujo del programa
def main():
	a = 1
	b = 4
	resultado = sumar(a,b)
	mensaje()
	print(resultado)
	
#Ejecutamos la funcion 'main()' que contiene a la funcion 'sumar()'
main()
	
#Nota: se puede ejecutar 'sumar()' directamente, pero es un buena practica usar 'main()' como el programa principal.
