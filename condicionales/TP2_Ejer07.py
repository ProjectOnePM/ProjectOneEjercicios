anio= (input("INGRESE AÑO A CALCULAR: "))

if anio.isdigit():
	anio_int= int(anio)
	if ( (anio_int%4)==0 and (anio_int%100)!=0 ) or (anio_int%400)==0:
		print("AÑO BISIESTO")
	else:
		print ("AÑO NO BISIESTO")
else:
	print("INGRESE SOLO NUMEROS")


