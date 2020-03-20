class Podlisty:
    def __init__(self, lista):
        self.lista = lista
    def stworz(self):
        podlisty = [[]]
        for i in range(len(self.lista) + 1):
            for j in range(i+1, len(self.lista)+1):
                pod = self.lista[i:j]
                podlisty.append(pod)
                podlisty.sort(key=len)
        return podlisty