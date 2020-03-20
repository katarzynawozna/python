def szyfrowanie(str):
    zaszyfrowane = ''
    klucz = {'a':'y', 'e':'i', 'i':'o', 'o':'a', 'y':'e'}
    for i in str:
        if i in klucz:
            zaszyfrowane += klucz[i]
        else:
            zaszyfrowane += i
    return zaszyfrowane

def odszyfrowanie(str):
    odszyfrowane = ''
    klucz = {'a':'y', 'e':'i', 'i':'o', 'o':'a', 'y':'e'}
    klucz_deszyfr = { klucz[k]:k for k in klucz}
    for i in str:
        if i in klucz_deszyfr:
            odszyfrowane += klucz_deszyfr[i]
        else:
            odszyfrowane += i
    return odszyfrowane
    


print(szyfrowanie('to jest moj tekst'))
print(odszyfrowanie('ta jist maj tikst'))

print(szyfrowanie('super tajny kod'))
print(odszyfrowanie('supir tyjne kad'))

print(szyfrowanie('przesylam ultra tajna wiadomosc specjalna dla pana prezydenta'))
print(odszyfrowanie('prziselym ultry tyjny woydamasc spicjylny dly pyny prizedinty'))