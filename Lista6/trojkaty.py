def czy_istnieje(a, b, c):
    #Sprawdza, czy taki trójkąt istnieje
    if a+b < c:
        return True
    elif a+c < b:
        return True
    elif c+b < a:
        return True
    else:
        return False

def obwod(a,b,c):
    #Liczy obwód trójkąta
    while()
        obwod_trojkata = a + b + c
        return obwod_trojkata

def pole(a, b, c):
    #Oblicza pole trójkąta
        p = (1/2*(obwod(a, b, c)))
        pole = 1/2**(p*((p-a)*(p-b)*(p-c)))
        return pole

def jaki_to_trojkat(a, b, c):
    #Czy jest to trójkąt równoboczny, równoramienny czy różnoboczny?
        if a == b == c:
            return "Jest to trójkąt równoboczny"
        elif a == b != c or b == c != a or a == b != c:
            return "Jest to trójkąt równoramienny!"
        else:
            return "To jest trójkąt różnoboczny!"

def katy_trojkata(a,b,c):
    #Jakie są kąty tego trójkąta?
        boki = [a, b, c]
        boki = sorted(boki)
        if (boki[2])**2 > (boki[0])**2 + (boki[1])**2:
            return "Jest to trojkąt rozwartokątny!"
        elif (boki[2])**2 == (boki[0])**2 + (boki[1])**2:
            return "Jest to trójkąt prostokątny"
        elif (boki[2])**2 < (boki[0])**2 + (boki[1])**2:
            return "Jest to trójkąt ostrokątny!"