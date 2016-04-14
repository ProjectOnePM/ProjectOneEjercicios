edad=(input("Por Favor Ingrese Edad: "))
anio_empleo=(input("Por Favor Años de Empleo: "))


if edad.isdigit() and anio_empleo.isdigit(): 
	
	edad_int=int(edad)
	anio_empleo_int=int(anio_empleo)

	if edad_int > anio_empleo_int:
		
		if edad_int>=60:
			
			if anio_empleo_int>=25:
					print (" Personas de jubilación por antigüedad adulta")
			else: 
					print("Personas adscriptas a la jubilación ")
		
		elif anio_empleo_int>=25 :
			print("Personas adscriptas por antigüedad joven")

		else:
				print("Personas no considerada")	
	else:
		print("LOS AÑOS DE EMPLEO NO PUEDEN SER MAYORES QUE LA EDAD")

else:	
	print ("DEBE INGRESAR SOLO DATOS NUMERICOS")