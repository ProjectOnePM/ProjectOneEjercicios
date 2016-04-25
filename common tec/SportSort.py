from control.control_digito import *
from control.control_letra import *
#Contadores
cantP=0
contH=0
contM=0


contMayorDeEdadM=0
contMenorDeEdadM=0

contMayorDeEdadH=0
contMenorDeEdadH=0

contMayorDeEdadMN=0
contMenorDeEdadMN=0

contMayorDeEdadHN=0
contMenorDeEdadHN=0

contHacenDeporte=0

#Booleanos
salir=False


print("")#Espacio
print("")#Espacio

print("-------Bienvenido Usuario-------") #Titulo 

while salir!=True:
	
	mientrasN=True
	mientras=True
	mientrasS=True
	mientrasE=True
	mientrasT=True

	print("")#Espacio
	print("")#Espacio

	while mientrasN==True:
		nombreApe=input("Ingrese nombre y apellido:")
		print("")
		controlN=esLetra(nombreApe)
		if controlN==1:
			mientrasN=False
		else:

			print ("Error! Ingreso equivocado")
			print(" ")

	
	while mientrasS==True:
		sexo=(input("Ingrese Sexo H/M: ")).upper()
		if(sexo=="H" or sexo == "M"):
			mientrasS=False
		else:
			print("Error! Ingreso equivocado")
			print("")#Espacio

	print(" ")

	while mientrasE==True:
		edad=(input("Ingrese la edad: "))
		controlE=esNumero(edad)
		if(controlE==1):
			edad=int(edad)
			if edad > 0 and edad < 100:
				mientrasE=False
			else:
				print("Error! fuera de rango")
				print("")
		else:
			print("Error! Ingreso equivocado")
			print("")#Espacio
	
	
	while mientras==True: #Verifica si se ingreso S o N, sino vuelve a recorrer
		print("")#Espacio
		haceDep=(input("Hace deporte S/N? ")).upper()

		if(haceDep=="S"):
			if(sexo=="H"):
				contH=contH+1
				mientras=False
				if(edad>1 and edad<18):
					contMenorDeEdadH=contMenorDeEdadH+1
					
				elif(edad>=18):
					contMayorDeEdadH=contMayorDeEdadH+1
					

			if(sexo=="M"):
				contM=contM+1
				mientras=False
				if(edad>1 and edad<18):
					contMenorDeEdadM=contMenorDeEdadM+1
					

				elif(edad>=18):
					contMayorDeEdadM=contMayorDeEdadM+1
					

		elif(haceDep=="N"):
			mientras=False
			if(sexo=="H"):
				if(edad>1 and edad<18):
					contMenorDeEdadHN=contMenorDeEdadHN+1
					
				elif(edad>=18):
					contMayorDeEdadHN=contMayorDeEdadHN+1
					

			if(sexo=="M"):
				if(edad>1 and edad<18):
					contMenorDeEdadMN=contMenorDeEdadMN+1
					

				elif(edad>=18):
					contMayorDeEdadMN=contMayorDeEdadMN+1
		else:
			print("Error! Ingreso equivocado!")
		
		
	cantP=cantP+1

	print("")#Espacio
	while mientrasT!=False:
		print("")
		print("Desea ingresar otra persona? ")

		terminar=((input("S/N: ")).upper())
		
		if terminar=="N":
			salir=True
			mientrasT=False
		if terminar=="S":
			mientrasT=False
		else:
			print("")
			print("Error! Ingreso equivocado!")

	
print("")#Espacio
print("")#Espacio
print("")#Espacio
print("-------------------------TOTAL GENERAL---------------------------------")
print("")#Espacio
print("El porcentaje de persona que no hacen deporte es de  %",(((cantP-(contH+contM))*100)/cantP))
print("")#Espacio
print("El porcentaje de personas que hacen deporte es de %",(((contH+contM)*100)/cantP))
print("")#Espacio
print("-------------------------TOTAL PARCIAL--------------------------------")
print("")#Espacio
if(contH>0):
	print("El porcentaje de hombres que hacen deporte es de %",((contH*100)/(contH+contM)))
	print("")
if(contM>0):
	print("El porcentaje de mujeres que hacen deporte es de %",((contM*100)/(contH+contM)))
	print("")

if((contH*100)/cantP>(contM*100)/cantP) and (contM>0) and (contH>0):
	print("Hay un mayor porcentaje de hombres que realizan deportes")
	print("")
elif ((contH*100)/cantP<(contM*100)/cantP) and (contM>0) and (contH>0):
	print("Hay un mayor porcentaje de mujeres que realizan deportes")

	print("")#Espacio
print("")#Espacio
print("----------------------------HOMBRES-----------------------------------")
print("")#Espacio
if(contH>0):
	print("El porcentaje de hombres mayores de edad que hacen deporte es de %",((contMayorDeEdadH*100)/contH))
	print(" ")
	print("El porcentaje de hombres menores de edad que hacen deporte es de %",((contMenorDeEdadH*100)/contH))
	print("")
	print("El porcentaje de hombres mayores de edad que NO deporte es de %",((contMayorDeEdadHN*100)/contH))
	print(" ")
	print("El porcentaje de hombres menores de edad que NO deporte es de %",((contMenorDeEdadHN*100)/contH))

print("")#Espacio

if(contH>0):
	if(contMayorDeEdadH*100)/contH>(contMenorDeEdadH*100)/contH:
		print("Hay un mayor porcentaje de hombres mayores de edad que realizan deporte")
	else:
		print("Hay un mayor porcentaje de hombres menores de edad que realizan deporte")


	print("")#Espacio

print("")#Espacio
print("---------------------------MUJERES----------------------------------")
print("")#Espacio
if(contM>0):
	print("El porcentaje de mujeres mayores de edad que hacen deporte es de %",((contMayorDeEdadM*100)/contM))
	print("")
	print("El porcentaje de mujeres menores de edad que hacen deporte es de %",((contMenorDeEdadM*100)/contM))
	print("")#Espacio
	print("El porcentaje de mujeres mayores de edad que NO hacen deporte es de %",((contMayorDeEdadMN*100)/contM))
	print("")
	print("El porcentaje de mujeres menores de edad que NO hacen deporte es de %",((contMenorDeEdadMN*100)/contM))
	print("")#Espacio

if(contM>0):
	if(contMayorDeEdadM*100)/contM>(contMenorDeEdadM*100)/contM:
		print("Hay un mayor porcentaje de mujeres mayores de edad que realizan deporte")
	else:
		print("Hay un mayor porcentaje de mujeres menores de edad que realizan deporte")



"""mostrar_tabla( (((contMayorDeEdadH*100))/contH),((contMenorDeEdadH*100)/contH ),((contMayorDeEdadM*100)/contM),((contMenorDeEdadM*100)/contM) )"""