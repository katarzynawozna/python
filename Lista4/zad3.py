import math

def konwersja_stopni(x, y=''):  
    if y == 'deg':
        x = (x*math.pi)/180
        return x
    elif y == 'rad':
        x = (x*180)/math.pi
        return x

