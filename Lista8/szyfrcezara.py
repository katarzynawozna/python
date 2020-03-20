def szyfrowanie(napis, n):
    zaszyfrowany = ''
    for litera in napis.lower():
            szyfr = ord(litera)
            if ord(litera) > 32:
                litera = chr((ord(litera) + n) % 256)
            zaszyfrowany += litera
    return zaszyfrowany

def odszyfrowywanie(napis, n):
    odszyfrowany = ''
    for litera in napis.lower():
            szyfr = ord(litera)
            if ord(litera) > 32:
                litera = chr((ord(litera) - n) % 256)
            odszyfrowany += litera
    return odszyfrowany