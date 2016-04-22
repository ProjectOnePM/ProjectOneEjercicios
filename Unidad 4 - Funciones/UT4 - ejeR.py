
#ejercicio r)
def edades(edad1,edad2):
	if int(edad1)>int(edad2):
		mayor=edad1
		distancia=int(edad1)-int(edad2)
		return mayor,distancia
	elif int(edad2)>int(edad1):
		mayor=edad2
		distancia=int(edad2)-int(edad1)
		return mayor,distancia
	else:
		return "SON IGUALES"


edad1=input("INGRESE EDAD: ")
print(" ")
edad2=input("INGRESE EDAD: ")

a,b=edades(edad1,edad2)
print(" ")
print("LA EDAD MAYOR ES: ",a)
print(" ")
print("LA DIFERENCIA ES DE :",b," años")
