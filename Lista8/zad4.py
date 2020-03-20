import os

plik = "PESEL.txt"
pesele = open(plik)
pesele = pesele.read()

pesele = pesele.split('\n')
del pesele[-1]

def sprawdzanie(x):
    liczba_kontrolna = ''
    liczba = int(x[0])*1
    liczba_kontrolna += str(liczba)[-1]
    liczba = int(x[1])*3
    liczba_kontrolna += str(liczba)[-1]
    liczba = int(x[2])*7
    liczba_kontrolna += str(liczba)[-1]
    liczba = int(x[3])*9
    liczba_kontrolna += str(liczba)[-1]
    liczba = int(x[4])*1
    liczba_kontrolna += str(liczba)[-1]
    liczba = int(x[5])*3
    liczba_kontrolna += str(liczba)[-1]
    liczba = int(x[6])*7
    liczba_kontrolna += str(liczba)[-1]
    liczba = int(x[7])*9
    liczba_kontrolna += str(liczba)[-1]
    liczba = int(x[8])*1
    liczba_kontrolna += str(liczba)[-1]
    liczba = int(x[9])*3
    liczba_kontrolna += str(liczba)[-1]

    liczba_kontrolna = liczba_kontrolna[-1]
    K = str(10 - int(liczba_kontrolna))
    K = K[-1]
    return K

def odczytywanie_pesel(pesel):
    odczyt = ''
    if (sprawdzanie(pesel) == pesel[-1]):
        m = pesel[2:4]
        if int(m) in list(range(21, 33)):
            y = "20" + pesel[:2]
            if int(m) in list(range(21,30)):
                m = list(m)
                m[0] = '0'
                m = ''.join(m)
            elif int(m) in list(range(30, 33)):
                m = list(m)
                m[0] = '1'
                m = ''.join(m)
        else:
            y = "19" + pesel[:2]
        d = pesel[4:6]
        plec = pesel[-2]
        if int(plec) % 2 == 0:
            plec = "KOBIETA"
        else:
            plec = "MĘŻCZYZNA"  
        odczyt += f"nr PESEL: {pesel} \n data urodzenia: {d}-{m}-{y}; \t płeć:{plec} \n"
    else:
        print("nah")
    return odczyt

plik = open("ODCZYT_PESELI.txt", "w+", encoding="utf-8")

for pesel in pesele:
    plik.write(odczytywanie_pesel(pesel))

plik.close()