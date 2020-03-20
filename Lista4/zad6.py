#korzystałam ze wzoru podanego na stronie https://www.rapidtables.com/convert/color/rgb-to-hsv.html

def rgb_to_hsv(r, g, b):
    R = r/255
    G = g/255
    B = b/255
    Cmax = max(R, G, B)
    Cmin = min(R, G, B)
    diff = Cmax - Cmin
    if diff == 0:
        H = 0
    elif Cmax == R:
        H = int(60*(((G-B)/diff)%6))
    elif Cmax == G:
        H = int(60*(((B-R)/diff)+2))
    elif Cmax == B:
        H = int(60*(((R-G)/diff)+4))
    if Cmax == 0:
        S = 0
    if Cmax != 0:
        S = int(100*(diff/Cmax))
    V = int(100*Cmax)
    return f'{H}*, {S}%, {V}%'
