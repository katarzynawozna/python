def look_n_say(n):
    if (n == 1):
        return "1"
    if (n == 2):
        return "11"
    
    baza = "11"
    for i in range(3, n + 1):
        baza += '#'
        l = len(baza)
        licznik = 1
        reszta = ""

        for j in range(1, l):

            if (baza[j] != baza[j - 1]):
                reszta += str(licznik + 0)
                reszta += baza[j - 1]
                licznik = 1
            else:
                licznik += 1
                
        baza = reszta
    
    return baza
