import random
import time


def bubble_sort(n):
    to_sort = [random.randint(0,20) for x in range(0, n)]
    for x in range(len(to_sort)):
        y = len(to_sort) - 1
        while y > x:
            if to_sort[y] < to_sort[y - 1]:
                to_sort[y], to_sort[y - 1] = to_sort[y - 1], to_sort[y]
            y -= 1
    return to_sort

start_time100 = time.time()
bubble_sort(100)
end_time100 = time.time()

print(f"Funkcja posortowała listę składającą się ze 100 elementów w {end_time100 - start_time100} sekund.")

start_time200 = time.time()
bubble_sort(200)
end_time200 = time.time()

print(f"Funkcja posortowała listę składajacą się z 200 elementów w {end_time200 - start_time200} sekund.")

start_time300 = time.time()
bubble_sort(300)
end_time300 = time.time()

print(f"Funkcja posortowała listę składajacą się z 300 elementów w {end_time300 - start_time300} sekund.")