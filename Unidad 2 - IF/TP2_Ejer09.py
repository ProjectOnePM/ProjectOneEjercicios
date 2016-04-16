import math
resp=(input("Elija que desea calcular 1:Triangulo/2:Circulo: ") ) 

if resp.isdigit() :
	
	if  resp=="1":
		
		base=(input("INGRESE BASE DEL TRIANGULO EN MTS: "))
		altura=(input("INGRESE ALTURA DEL TRIANGULO EN MTS: "))

		
		if float(base) and float(altura):

			base_int=float(base)
			altura_int=float(altura)
			area= (base_int*altura_int)/2
			print("EL AREA DEL TRIANGULO ES: ", area)
		else:
			print("DEBE INGRESAR DATOS NUMERICOS")

	elif resp=="2":
		
		radio=(input("INGRESE BASE DEL CIRCULO EN MTS: "))

		if float(radio) :
			radio_int=float(radio)
			area= math.pi * (pow(radio_int, 2))
			print("EL RADIO DEL CIRCULO ES: ", area)
		else:
			print("DEBE INGRESAR DATOS NUMERICOS")
			
	else:
		print("DEBE INGRESAR 1:Triángulo/2:Circulo")
else:
	print("DEBE INGRESAR DATOS NUMERICOS")

