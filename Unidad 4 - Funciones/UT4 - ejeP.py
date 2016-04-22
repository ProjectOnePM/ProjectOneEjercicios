#ejercicio p)
def suma_digito(n):
	total=0
	
	for i in n:
		total +=int(i) 
	return total

digito=input('Ingrese Digito: ')

print(suma_digito(digito))



