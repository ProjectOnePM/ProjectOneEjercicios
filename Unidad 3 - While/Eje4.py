cuentas=[]
contrasenas=[]
for x in range(0,14):
	nombre=raw_input("ingrese el nombre de la cuenta:  ")
	dominio=raw_input("ingrese el dominio: @")
	contrasena1=raw_input("ingrese contrasena:  ")
	contrasena2=raw_input("vuelva a ingresar contrasena:  ")
	while (contrasena1!=contrasena2):
		print "las contrasenas no coinciden vuelva a intentarlo"
		contrasena1=raw_input("ingrese contrasena:  ")
		contrasena2=raw_input("vuelva a ingresar contrasena:  ")
	contrasenas.append(contrasena1)
	cuentas.append(("%s@%s")%(nombre,dominio))
for y in range(0,14):
	print ("cuenta numero %d, nombre: %s, contrasena: %s")%(y+1,cuentas[y],contrasenas[y])
