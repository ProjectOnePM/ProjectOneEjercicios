"""comprobador de digitos"""
def esLetra(a):
	a=a.upper()
	letra=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Ñ','.',' ']
	bandera=False
	for i in range(0,len(a)):
		if (a[i] not in letra):
			bandera=True
	if bandera:
		return 0
	else:
		return 1







