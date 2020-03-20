import szyfrcezara
import time
import os

obecny_katalog = os.getcwd()
print("Obecnie znajdujesz się w katalogu: ", obecny_katalog)

while(True):
    try:
        katalog_zplikiem = input("Podaj ścieżkę do katalogu, gdzie znajduje się plik do odszyfrowania: ")
        break
    except FileExistsError as e:
        print(e, "Nie istnieje taki katalog/błędna ścieżka.")

os.chdir(katalog_zplikiem)
lista_plikow = os.listdir(katalog_zplikiem)

try:
    for x in range(0, len(lista_plikow)):
        if 'plik_zaszyfrowany' in lista_plikow[x]:
            plik = lista_plikow[x]
        else:
            raise FileExistsError
except FileExistsError as e:
    print(e, "W tym katalogu nie znajduje się zaszfyrowany plik tekstowy.")
    plik_do_odszyfrowania = input("Podaj tekst do odszyfrowania")



if plik[18] == '0':
    n = 10
else:
    n = int(plik[17])

try:
    plik_odczyt = open(plik)
    plik_do_odszyfrowania = plik_odczyt.read()
finally:
    plik_odczyt.close()

do_zapisu = szyfrcezara.odszyfrowywanie(plik_do_odszyfrowania, n)

def zapisywanie_tekstu(do_zapisu):
    data = time.strftime("%Y_%m_%d")
    nazwa_pliku = f"plik_deszyfrowany{n}_{data}.txt"
    while(True):
        try:
            katalog = input("Podaj katalog(ścieżkę do katalogu), w którym chcesz zapisać zaszyfrowaną wiadomość: ")
            plik = open(katalog + "\\" + nazwa_pliku, "w+", encoding="utf-8")
            plik.write(do_zapisu)
            plik.close()
            break
        except FileNotFoundError as e:
            print(e, "Taki katalog nie istnieje")
            try:
                wybor = input("Czy chcesz go stworzyć? T/N")
                wybor = wybor.lower()
                try:
                    if wybor == 't':
                        os.mkdir(katalog)
                        plik = open(katalog + "\\" + nazwa_pliku, "w+", encoding="utf-8")
                        plik.write(do_zapisu)
                        plik.close()
                        break
                    elif wybor == 'n':
                        print("Wybierz katalog docelowy ponownie.")
                        continue
                    else:
                        raise ValueError
                except PermissionError as e:
                    print(e, "Program nie ma uprawnień do tworzenia nowych katalogów w tym miejscu")
                    continue
            except ValueError:
                print("Wprowadź 't' lub 'n'. Plik nie został nigdzie zapisany.")
                continue


zapisywanie_tekstu(do_zapisu)