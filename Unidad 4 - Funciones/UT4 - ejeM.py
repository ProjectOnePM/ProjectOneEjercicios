def rango(l1,l2,x):
	if ((l2>=x)and(l1<=x)):
		a=(l2-l1)/2
		if (a>=x):
			return 2
		else:
			return 1
	else:
		return 0


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