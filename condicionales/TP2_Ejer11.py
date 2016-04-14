
mes=input("¿Asistio todo el mes? 1:SI/2:NO : ")
horas=input("¿Cuantas horas asistio domingos ? : ")

if mes.isdigit() and horas.isdigit() :
	horas_int=int(horas)

	if mes=="2":
		if horas_int>= 3 and horas_int<= 10:
			print("ADICIONAL 2%")
		else:
			print("CASO NO CONSIDERADO")
	elif  mes=="1":
			if horas_int >= 3 and horas_int <= 5:
				print ("ADICIONAL 3%")
			elif horas_int >=6 and horas_int<=10:
				print("ADICIONAL 10%")
			else:
				print("CASO NO CONSIDERADO")
	else:
		print("DEBE INGRESAR VALORES NUMERICOSS")

else:
	print ("DEBE INGRESAR DATOS NUMERICOS Y VALORES ENTRE 1 o 2 ")
