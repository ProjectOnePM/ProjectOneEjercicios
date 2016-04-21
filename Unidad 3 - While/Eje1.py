Saldo=0
operacion="si";
while (operacion=="si"):
	operacion = raw_input("desea hacer un deposito o un retiro? ")
	if (operacion == "retiro"):
		cantidad = input("Por favor ingrese la cantidad que desea retirar de su cuenta: $")
		if (cantidad <= Saldo):
			Saldo = Saldo - cantidad
			print "Se desconto de su cuenta su retiro!. su saldo es: $",Saldo
		else:
			print "No tiene cantidad suficiente para retirar, vuelva a intentarlo."
	if (operacion == "deposito"):
		deposito = input("Por favor ingrese la cantidad a depositar: $")
		Saldo = Saldo + deposito
		print "Se realizo deposito, en su cuenta tiene disponible ahora: $",Saldo
	operacion = raw_input("Desea realizar otra operacion? si/no: ")
print "Saldo total: $",Saldo


