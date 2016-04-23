#h) Escriba una funcin que permita obtener el promedio de los n nmeros naturales.

def funcionprom(n):
	suma = 0
	cont = 0
	for i in range(1, n):
		suma=suma+i
		cont=cont+1
		sum=suma/cont
	return sum




