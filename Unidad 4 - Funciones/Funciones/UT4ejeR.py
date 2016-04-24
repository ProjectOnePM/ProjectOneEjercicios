def primo_no_primo():
	opcion="SI"
	while True:
		try:
			print(" ")
			num=input('INGRESE UN NUMERO NATURAL (NO)--->SALIR: ')
			
			if num=='NO' or num=='no':
				break
			elif (es_primo(int(num))):
				print("EL NUMERO %s ES PRIMO" %num , " Y SU FACTORIA ES: " , factorial(int(num)))
			else:
				print("EL NUMERO %s NO ES PRIMO" %num, "Y SUS MULTIPLOS SON: ")
				multiplos_resul=multiplos(int(num))
				for i in range(0,len(multiplos_resul)):
					print("NUMERO: ", multiplos_resul[i])
		except:
			print(" El NUMERO TIENE QUE SER UN NUMERO NATURAL")


def es_primo(var):
	for i in range(2,var):
		if (var%i)==0:
			return False
		else:
			return True

def factorial(var):
	fact=1
	for i in range(1,var):
		fact= fact + (fact*i)
	return fact

def multiplos(var):
	lista_multiplos=[]
	for i in range(1,var):
		if var%i == 0:
			lista_multiplos.append(i)
	return lista_multiplos


