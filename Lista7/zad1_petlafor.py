import time


def fibbonacci_for(n):
    a1 = 0
    a2 = 1
    for x in range(0, n):
        print(a1)
        temp = a1
        a1 = a2
        a2 = temp + a2
    return a1

start1 = time.time()
print(fibbonacci_for(15))
koniec1 = time.time()
wynik1 = koniec1 - start1

print(f"Funkcja napisana przy pomocy pętli for wykonała się w {wynik1} sekund.")