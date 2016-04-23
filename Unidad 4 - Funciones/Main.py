from Funciones.UT4ejeF import *
from Funciones.UT4ejeG import *
from Funciones.UT4ejeH import *
from Funciones.UT4ejeK import *
from Funciones.UT4ejeL import *
from Funciones.UT4ejeM import *
from Funciones.UT4ejeN import *
from Funciones.UT4ejeO import *
from Funciones.UT4ejeP import *
from Funciones.UT4ejeQ import *
from Funciones.UT4ejeR import *
from Funciones.UT4ejeT import *
op='s'
Salir=['s','n']
Lista=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t"]
while (op!='n'):
	print "---------Menu ejercicios Funciones---------"
	print ""
	print "a - Ejercicio A : calculo de naturales k"
	print "b - Ejercicio B : sumatoria de naturales k"
	print "c - Ejercicio C : naturales par imprimirlos impar imprimirlos al revez"
	print "d - Ejercicio D : potencia a b con multiplicaciones sucesivas"
	print "e - Ejercicio E : factorial "
	print "f - Ejercicio F : superficie cono"
	print "g - Ejercicio G : pasar a mayuscula"
	print "h - Ejercicio H : promedio"
	print "i - Ejercicio I : suma de divisores"
	print "j - Ejercicio J : divisores de los impares n"
	print "k - Ejercicio K : numero harmonico"
	print "l - Ejercicio L : area y superficie de un cuadrado"
	print "m - Ejercicio M : numero en rango"
	print "n - Ejercicio N : conversor de dos unidades"
	print "o - Ejercicio O : encontrar suma"
	print "p - Ejercicio P : suma de los digitos de un numero de dos cifras"
	print "q - Ejercicio Q : numero y string comprobando longitud"
	print "r - Ejercicio R : numeros primos factorial"
	print "s - Ejercicio S : edades"
	print "t - Ejercicio T : cambio"
	eje=""
	print ""
	while (eje not in Lista):
		eje=raw_input("Que ejercicio desea ejecutar: ")
	print ""
	print ("------------Ejercicio %s-------------")%(eje)
	if (eje=='a'):
		print "aun no se codifico"
	elif(eje=='b'):
		print "falta hacer"
	elif(eje=='c'):
		print "Falta hacer"
	elif(eje=='d'):
		print "Falta hacer"
	elif(eje=='e'):
		print "Falta hacer"
	elif(eje=='f'):
		ra=input("Ingrese radio de la base : " )
		ga=input("Ingrese generatriz del cono: " )
		t= funcionCono(ra,ga)
		print "La superficie del cono es: ", t
	elif(eje=='g'):
		pepe=raw_input("Ingrese un Caracter ")
		funcion_Mayuscula(pepe)
	elif(eje=='h'):
		n=input("Ingrese numero que desee sacar el promedio:")
		total=funcionprom(n)
		print "Promedio de los numeros es:",total
	elif(eje=='i'):
		print "Falta hacer"
	elif(eje=='j'):
		print "Falta hacer"
	elif(eje=='k'):
		h=float(input("ingrese el numero armonico que desea calcular: "))
		har=harmonico(h)
		print "el numero harmonico es: ",har
	elif(eje=='l'):
		lado=input("ingrese el lado del cuadrado: ")
		per=perimetroCuadrado(lado)
		area=areaCuadrado(lado)
		print ("area = %d perimetro = %d")%(area,per)
	elif(eje=='m'):
		l1=input("ingrese el rango inicial: ")
		l2=input("ingrese el rango final: ")
		n=input("ingrese el numero x a determinar: ")
		busqueda=rango(l1,l2,n)
		if (busqueda == 1):
			print "si esta en rango y esta a la derecha"
		elif (busqueda == 2):
			print "si esta en rango y esta a la izquierda"
		else:
			print "no esta en rango"
	elif(eje=='n'):
		l1=input("ingrese los metros que desea calcular a pulgadas: ")
		l2=input("ingrese las pulgadas a calcular a pies: ")
		pul=metroapulgada(l1)
		pie=pulgadaapie(l2)
		print ("%smetros = %spulgadas")%(l1,pul)
		print ("%spulgadas = %spies")%(l2,pie)
	elif(eje=='o'):
		a=input("ingrese el primer numero: ")
		b=input("ingrese el segundo numero: ")
		c=input("ingrese el tercer numero: ")
		busqueda=encontrarsuma(a,b,c)
		print busqueda
	elif(eje=='p'):
		digito=input('Ingrese Digito: ')
		print(suma_digito(digito))
	elif(eje=='q'):
		palabra= input("INGRESE STRING: ")
		print ""
		entero = input("INGRESE NUMERO: ")
		print(entero_string(palabra,entero))
	elif(eje=='r'):
		edad1=input("INGRESE EDAD: ")
		print(" ")
		edad2=input("INGRESE EDAD: ")

		a,b=edades(edad1,edad2)
		print(" ")
		print("LA EDAD MAYOR ES: ",a)
		print(" ")
		print("LA DIFERENCIA ES DE :",b," anios")
	elif(eje=='s'):
		print "falta ejercicio s"
	else:
		digito=input('Ingrese Digito: ')
		print(suma_digito(digito))
	op=""
	while (op not in Salir):
		op=raw_input("Desea ejecutar otro ejercicio?  s/n : ")





