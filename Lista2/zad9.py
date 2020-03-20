from itertools import chain

lista_początkowa = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
lista = list(chain.from_iterable(lista_początkowa))
print(lista)