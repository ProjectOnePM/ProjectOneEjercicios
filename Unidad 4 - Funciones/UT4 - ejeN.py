def metroapulgada(a):
	return (a*39.37)

def pulgadaapie(a):
	return (a*12.0)

l1=input("ingrese los metros que desea calcular a pulgadas: ")
l2=input("ingrese las pulgadas a calcular a pies: ")
pul=metroapulgada(l1)
pie=pulgadaapie(l2)
print ("%smetros = %spulgadas")%(l1,pul)
print ("%spulgadas = %spies")%(l2,pie)