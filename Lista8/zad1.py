import os
import time
import szyfrcezara

try:
    plik = open('plik_do_zaszyfrowania.txt')
except FileExistsError:
    print("Nie istnieje taki plik!")
    napis_do_zaszyfrowania = input("Podaj tekst, który chcesz zaszyfrować: ")


try:
    napis_do_zaszyfrowania = plik.read()

finally:
    plik.close()

while (True):
    try:
        n = int(input("Podaj przesunięcie według którego ma być zaszyfrowany tekst(1-10): "))
        break
    except ValueError as e:
        print("Błąd typu wartośći ", e)
        n = input("Wprowadź wartość przesunięcia ponownie: ")

do_zapisania = szyfrcezara.szyfrowanie(napis_do_zaszyfrowania, n)

def zapisywanie_tekstu(do_zapisu):
    data = time.strftime("%Y_%m_%d")
    nazwa_pliku = f"plik_zaszyfrowany{n}_{data}.txt"
    while(True):
        try:
            katalog = input("Podaj katalog(ścieżkę do katalogu), w którym chcesz zapisać zaszyfrowaną wiadomość: ")
            plik = open(katalog + "\\" + nazwa_pliku, "w+", encoding="utf-8")
            plik.write(do_zapisu)
            plik.close()
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

zapisywanie_tekstu(do_zapisania)

