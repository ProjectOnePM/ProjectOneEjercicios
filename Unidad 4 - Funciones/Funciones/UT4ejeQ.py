#ejercicio q)
def entero_string(s,n):
	s_sin_espacio=s.replace(" ", "")#borra espacio
	if len(s_sin_espacio)==int(n):
		print("ES IGUAL")
	else:
		print("NO IGUAL")

