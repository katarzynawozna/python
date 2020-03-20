def suma_szeregu(n):
	x = 1
	suma = 0
	while x in range(1, int(n)+1):	
		suma += 1/x
		x += 1
	return suma

n = input("Podaj liczbę n: ")
suma_szeregu(n)	
