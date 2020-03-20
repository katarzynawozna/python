def permutacja(lista): 
    if len(lista) == 0: 
        return [] 
    if len(lista) == 1: 
        return [lista] 
    l = [] 
    for i in range(len(lista)): 
       poczatek = lista[i] 
       reszta = lista[:i] + lista[i+1:] 
       for p in permutacja(reszta): 
           l.append([poczatek] + p) 
    return l 
    for p in permutacja(lista): 
        print (p) 


