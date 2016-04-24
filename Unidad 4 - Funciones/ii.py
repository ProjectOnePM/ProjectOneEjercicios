n=input("Ingrese el numero: ")
sum=0
for i in range(1,(n/2)+1):
        if n%i == 0:
            sum=sum+i
if n==sum:
	print"Es un numero perfecto"
elif (n<sum):
	print"Es un numero abundante"
elif (n>sum):
	print"Es un numero deficiente"

