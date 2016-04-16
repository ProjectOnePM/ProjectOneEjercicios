print "--------------------ejercicio7--------------------------"
print ""
fulano=input("ingrese cuanto invirtio fulano")
mengano=input("ingrese cuanto invirtio mengano")
sultano=input("ingrese cuanto invirtio sultano")
total_invertido=sultano+mengano+fulano
porcenta_de_fulano = (fulano) / float (total_invertido) *100
porcenta_de_mengano= (mengano) / float (total_invertido) *100
porcenta_de_sultano= (sultano) / float (total_invertido) *100
print "mengano invirtio %.1f%%" % porcenta_de_fulano
print "fulano invirtio" ,str('{0:.3g}'.format(porcenta_de_fulano))+"%"
print "sultano invirtio" ,str('{0:.3g}'.format(porcenta_de_sultano))+"%"
print ""
print "-----------------------FIN------------------------------"
	