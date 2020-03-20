import random
import os

# informacje na temat generowania numeru pesel zaczerpnięte ze strony https://obywatel.gov.pl/dokumenty-i-dane-osobowe/czym-jest-numer-pesel

def generator_peseli():
    pesel = ""

    rok_urodzenia = [str(random.randint(1900, 2099)) for x in range(10)]
    i = random.randint(0, len(rok_urodzenia)-1)
    rok = rok_urodzenia[i]
    pesel += str(rok[2:])

    if int(rok) > 1999:
        miesiac_urodzenia = [random.randint(21, 32) for x in range(10)]
    else:
        miesiac_urodzenia = [random.randint(1, 12) for x in range(10)]

    j = random.randint(0, len(miesiac_urodzenia)-1)
    miesiac = miesiac_urodzenia[j]
    if miesiac_urodzenia[j] in range(0, 10):
        pesel += "0" + str(miesiac)
    else:
        pesel += str(miesiac)

    if (miesiac == 2 or miesiac == 22) and ((int(rok) % 4 == 0 or int(rok) % 100 != 0) or int(rok) % 400 == 0):
        dzien_urodzenia = [random.randint(1, 30)]
        przystepny = random.randint(0, len(dzien_urodzenia)-1)
        dzien = dzien_urodzenia[przystepny]
    else:
        dzien_urodzenia = [random.randint(1,31) for x in range(10)]
        k = random.randint(0, len(dzien_urodzenia)-1)
        dzien = dzien_urodzenia[k]

    if dzien in range(1, 10):
        pesel += "0" + str(dzien)
    else:
        pesel += str(dzien)

    liczba_porzadkowa = [random.randint(0,9) for x in range(0,10)]
    for y in range(4):
        l = random.randint(0, len(liczba_porzadkowa)-1)
        liczba = liczba_porzadkowa[l]
        pesel += str(liczba)

    liczba_kontrolna = ''
    liczba = int(pesel[0])*1
    liczba_kontrolna += str(liczba)[-1]
    liczba = int(pesel[1])*3
    liczba_kontrolna += str(liczba)[-1]
    liczba = int(pesel[2])*7
    liczba_kontrolna += str(liczba)[-1]
    liczba = int(pesel[3])*9
    liczba_kontrolna += str(liczba)[-1]
    liczba = int(pesel[4])*1
    liczba_kontrolna += str(liczba)[-1]
    liczba = int(pesel[5])*3
    liczba_kontrolna += str(liczba)[-1]
    liczba = int(pesel[6])*7
    liczba_kontrolna += str(liczba)[-1]
    liczba = int(pesel[7])*9
    liczba_kontrolna += str(liczba)[-1]
    liczba = int(pesel[8])*1
    liczba_kontrolna += str(liczba)[-1]
    liczba = int(pesel[9])*3
    liczba_kontrolna += str(liczba)[-1]

    liczba_kontrolna = liczba_kontrolna[-1]
    K = 10 - int(liczba_kontrolna)
    
    pesel += str(K)[-1]
    
    return pesel

plik = open("PESEL.txt", "w+", encoding="utf-8")

for x in range(10):
    plik.write(generator_peseli() + "\n")

plik.close()