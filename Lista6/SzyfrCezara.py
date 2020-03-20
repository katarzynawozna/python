def szyfrowanie(napis):
#szyfruje napis według Szyfru Cezara, zamienia litere alfabetu na następną, czyli +1;
    napis = str(napis)
    zaszyfrowany = ''
    for litera in napis.lower():
        if ord(litera) in range(97, 122):
            szyfr = ord(litera)
            szyfr += 1
            zaszyfrowany += chr(szyfr)
        elif ord(litera) == 122:
            szyfr = 97
            zaszyfrowany += chr(szyfr)
        else:
            zaszyfrowany += litera
    return zaszyfrowany

def odszyfrowywanie(napis):
#odszyfrowuje napis według Szyfru Cezara
    napis = str(napis)
    odszyfrowany = ''
    for litera in napis.lower():
        if ord(litera) in range(98,123):
            szyfr = ord(litera)
            szyfr -= 1
            odszyfrowany += chr(szyfr)
        elif ord(litera) == 97:
            szyfr = chr(122)
            odszyfrowany += szyfr
        else:
            odszyfrowany += litera
    return odszyfrowany