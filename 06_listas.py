#!/usr/bin/env python
'''
Creado el 08.04.2018

@author: Maximiliano R Soria
@version: 1.0 
@note: Creado para la catedra de Programacion en tiempo real.

'''

#Una lista es una coleccion de valores almacenados.

miLista=["pepe", "Manuel","Paola"]

#Mostrar una lista
print("\nMostrar una lista\nMi lista es:")
print(miLista)

#Alta de elemento en una lista
miLista.append("Maxi")
print("\nAlta de elemento en una lista\nMi lista es:")
print(miLista)

#Modificar un elemento a la lista 
miLista[0] = "Pepe" 
print("\nModificar un elemento a la lista\nMi lista es:")
print(miLista)
#Nota: '[0]' indica en que indice nos estamos parando, los indices comienzan desde 0 

#Baja de un elemento en la lista
del(miLista[0])
print("\nBaja de un elemento en la lista\nMi lista es:")
print(miLista)

#Consultar/Recorrer lista
nombre = raw_input("\nConsultar/Recorrer lista \n\nIngrese un nombre: ")
for x in miLista:	
	if (nombre == x):
		print ( "\nEl nombre existe dentro de la lista!")
		break
#Nota: Break corta la iteracion del ciclo for

#Imprimir cada elemento de la lista con while
indice = 0
print("\nImprimir cada elemento de la lista con while\nMi lista es:")
while(indice<len(miLista)):
	print(miLista[indice])
	indice = indice + 1
	

#Imprimir cada elemento de la lista con for
print("\nImprimir cada elemento de la lista con for\nMi lista es:")
for x in miLista:
	print(x)
	
#Metodo dos
print("\nImprimir cada elemento de la lista con for\nMi lista es:")
for y in range(0,len(miLista)):
	print(miLista[y])
