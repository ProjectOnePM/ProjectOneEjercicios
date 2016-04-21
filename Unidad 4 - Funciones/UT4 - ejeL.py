def perimetroCuadrado (a):
	return a*4

def areaCuadrado(a):
	return (a*2)**2

lado=input("ingrese el lado del cuadrado: ")
per=perimetroCuadrado(lado)
area=areaCuadrado(lado)
print ("area = %d perimetro = %d")%(area,per)