
op_mes=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
total_general=0
opcion="si"
nombre=""
while opcion=="si":
	nombre=raw_input("Ingrese el nombre del vendedor: ")
	total_parcial=0
	for x in range(0,12):
		mes=input(("Por favor ingrese el monto vendido en el mes %s : $")%(op_mes[x]))
		total_parcial=mes+total_parcial
	total_general=total_general+total_parcial
	print ""
	print "el total vendido de ",nombre,"es de $",total_parcial
	opcion=raw_input("desea seguir calculando las ventas de otro vendedor? si/no : ")
	if (opcion=="no"):
		print "total general recaudado : $",total_general
		break

