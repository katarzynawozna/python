N = int(input("Podaj indeks ostatniego wyrazu: "))

fibonacci = [0,1]
for x in range(N-1):
     fibonacci.append(fibonacci[-2] + fibonacci[-1])
print(fibonacci)
