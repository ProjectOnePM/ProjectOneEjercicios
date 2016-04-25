"""comprobador de digitos"""
def esNumero(a):
	puntos=0
	digito=['0','1','2','3','4','5','6','7','8','9','.']
	bandera=False
	for i in range(0,len(a)):
		if (a[i] not in digito):
			bandera=True
		if (a[i] =='.'):
			puntos=puntos + 1
			if puntos==2:
				bandera=True
	if bandera:
		return 0
	else:
		if (puntos == 1):
			return 2
		else:
			if a!="":
				return 1
			else:
				return 4







