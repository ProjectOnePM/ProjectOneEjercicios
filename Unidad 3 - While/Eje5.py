animal=raw_input("por favor ingrese el tipo de animal que desea analizar: elefantes / jirafas / chimpances")
if (animal=="elefantes"):
	cantidad=20
elif(animal=="jirafas"):
	cantidad=15
elif(animal=="chimpances"):
	cantidad=40
else:
	print "error no eligio una opcion correcta vuelva a ejecutar el programa"
C1=0;
C2=0;
C3=0;
while (cantidad!=0):
	edad=input(("por favor ingrese un numero segun corresponda la edad del %s: \n 1 - de 0..1 anios \n 2 - de 0..3 anios \n 3 - 3..mas anios \n opcion: ")%(animal))
	print "restan: ",cantidad
	cantidad=cantidad-1
	if (edad==1):
		C1=C1+1
	elif (edad==2):
		C2=C2+1
	elif (edad==3):
		C3=C3+1
	else:
		print("no ingreso correctamente un rango de edad, vuelva a ingresarlo")
		cantidad=cantidad+1
total=C1+C2+C3
print ""
print "animal: ",animal
print "total de 0 a 1 anios: ",(float(C1)/total)*100,"%"
print "total de 1 a 3 anios: ",(float(C2)/total)*100,"%"
print "total de mas de 3 anios: ",(float(C3)/total)*100,"%"