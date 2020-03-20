import sys
import numpy as np

try:
    dane_pomiarowe = sys.argv[1]
except IndexError:
    dane_pomiarowe = sys.stdin.read()

def statystyka(dane_pomiarowe):
    dane_pomiarowe = dane_pomiarowe.split(',')
    dane_pomiarowe = list(map(int, dane_pomiarowe))
    srednia  = np.mean(dane_pomiarowe)
    dane_pomiarowe = np.array(dane_pomiarowe)
    wariancja = np.var(dane_pomiarowe)
    odchylenie = np.std(dane_pomiarowe)
    print(f"Średnia tych danych wynosi {srednia}, wariancja {wariancja} a odchylenie standardowe {odchylenie}.")

statystyka(dane_pomiarowe)