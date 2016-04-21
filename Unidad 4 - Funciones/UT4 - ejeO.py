def encontrarsuma(a,b,c):
	if ((a+b)==c):
		return ("La suma de %s + %s = %s")%(a,b,c)
	elif ((a+c)==b):
		return ("La suma de %s + %s = %s")%(a,c,b)
	elif ((b+c)==a):
		return ("La suma de %s + %s = %s")%(b,c,a)
	else:
		return ("No hay dos numeros que se sumen y el tercero sea el resultado")

a=input("ingrese el primer numero: ")
b=input("ingrese el segundo numero: ")
c=input("ingrese el tercer numero: ")
busqueda=encontrarsuma(a,b,c)
print busqueda