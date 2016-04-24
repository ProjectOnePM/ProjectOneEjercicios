def funcionnumero(n):
	sum=0
	for i in range(1,(n/2)+1):
     		if n%i==0:
     	   		sum=sum+i
	if n==sum:
		return"Es un numero perfecto"
	elif (n<sum):
		return"Es un numero abundante"
	elif (n>sum):
		return"Es un numero deficiente"

