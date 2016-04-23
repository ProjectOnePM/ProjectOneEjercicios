def rango(l1,l2,x):
	if ((l2>=x)and(l1<=x)):
		a=(l2-l1)/2
		if (a>=x):
			return 2
		else:
			return 1
	else:
		return 0


