from math import trunc
def vuelto_billites(dinero):
	billetes=[100,50,20,10,5,2,1] 

	for i in billetes:
		if int(dinero/i)>0:
			print("Necesita ", trunc(dinero/i), " de ", i)
			dinero=dinero%i 	
			