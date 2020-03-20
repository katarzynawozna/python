x1 = int(input('Podaj pierwszą współrzędną pierwszego punktu: '))
y1 = int(input('Podaj drugą współrzędną pierwszego punktu: '))
x2 = int(input('Podaj pierwszą współrzędną drugiego punktu: '))
y2 = int(input('Podaj drugą współrzędną drugiego punktu: '))

def odleglosc_punktu(x1, y1, x2, y2):
    a = (x1-x2)**2
    b = (y2-y1)**2
    odleglosc = (a+b)**(1/2)
    return odleglosc