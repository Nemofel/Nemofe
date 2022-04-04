X = int(input('veuillez choisir le nombres de lignes ?'))
Y = int(input('veuillez choisir le nombres de colonnes ?'))

Colonnes = Y
lignes = X 

C = 0
L = 0

while L < X :
	while C < Y :
		print("@",end="")
		C = C + 1
	print("")
	L = L + 1
	C=0