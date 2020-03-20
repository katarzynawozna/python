class CiagArytmetyczny:
    def __init__(self, a1, r, n=1):
        self.a1 = a1
        self.r = r
        self.wyrazy = [a1]
        
        if n > 1:
            self.generate(n-1)

    def generate(self, n):
        for x in range(n):
            self.wyrazy.append(self.wyrazy[-1] + self.r)
        
    def __iter__(self):
        for a in self.wyrazy:
            yield a

    def __len__(self):
        return len(self.wyrazy)

    def __str__(self):
        s = "Ciąg arytmetyczny ({a1}, {r}):".format(a1=self.a1, r=self.r)

        for wyraz in self:
            s += " " + str(wyraz) 
        return s   

    def save(self, filename):
        with open(filename, 'w') as f:
            f.write(self.__str__())
