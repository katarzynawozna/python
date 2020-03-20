def mnozenie_dodawanie(list):
	mnozenie = 1
	dodawanie = 0
	for x in list:
		dodawanie += x
		mnozenie = mnozenie*x
	return dodawanie, mnozenie