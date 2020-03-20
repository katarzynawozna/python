import time

def fibbonacci_rek(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibbonacci_rek(n-1) + fibbonacci_rek(n-2)

n = int(input("Proszę podać, do którego wyrazu podać ciąg Fibonacciego: "))

start2 = time.time()
for i in range(1, n+1):
    print(fibbonacci_rek(i))
koniec2 = time.time()

wynik2 = koniec2 - start2

print(f"Funkcja napisana rekurencyjnie wykonała sie w {wynik2} sekund.")