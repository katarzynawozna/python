lista_do_uporządkowania = [(2, 8), (5, 5), (9, 3), (1, 0), (3, 2), (6, 4), (1, 9), (10, 3), (2, 3), (1, 7)]
uporządkowana = sorted(lista_do_uporządkowania, key=lambda x: x[1])
print(uporządkowana)