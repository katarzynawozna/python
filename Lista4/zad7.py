def trojkat_pascala(n):
	trojkat = [1]
	for i in range(n):
		print(f'Wiersz {i+1}: {trojkat}')
		nowaLista = []
		nowaLista.append(trojkat[0])
		for i in range(len(trojkat) - 1):
			nowaLista.append(trojkat[i] + trojkat[i+1])
		nowaLista.append(trojkat[-1])
		trojkat = nowaLista
