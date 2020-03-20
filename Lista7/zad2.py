import random
import time

def insert_sort(n):
    to_sort = [random.randint(0,20) for x in range(0, n)]
    for x in range(1, len(to_sort)):
        key = to_sort[x]
        j = x - 1
        while j >= 0 and to_sort[j] > key:
            to_sort[j+1] = to_sort[j]
            j = j - 1
        to_sort[j + 1] = key

start_time100 = time.time()
insert_sort(100)
end_time100 = time.time()

print(f"Dla 100 elementów listy funkcja posortowała je w {end_time100 - start_time100} sekund.")

start_time200 = time.time()
insert_sort(200)
end_time200 = time.time()

print(f"Dla 200 elementów listy funkcja posortowała je w {end_time200 - start_time200} sekund.")

start_time300 = time.time()
insert_sort(300)
end_time300 = time.time()

print(f"Dla 300 elementów listy funkcja posortowała je w {end_time300 - start_time300} sekund.")
