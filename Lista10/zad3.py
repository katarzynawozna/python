from itertools import permutations

class ListaLiczbRzeczywistych:
    def __init__(self, lista):
        self.lista = lista
    def zbiory(self):
        zbiory = []
        permutacje = list(permutations(self.lista, 3))
        for wariant in permutacje:
            if sum(wariant) == 0:
                zbiory.append(list(wariant))
        return zbiory