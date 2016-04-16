impor_total =input("Ingrese impor_total: ")
impuestos_app =input("Ingrese impuestos aplicados : ")


impor_neto = impor_total - impuestos_app

if impor_neto <=0 :
		print("Error ")

elif  impor_total > 5000  :
		print("Monto Superado para Consumidor Final")
else:
	print("CASO NO CONSIDERADO")


