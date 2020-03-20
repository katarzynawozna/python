j = list(range(11))
i = int(input("Proszę podać jakąś cyfrę: "))

for x in range(len(j)):
	for y in range(1,len(j)):
		print(f"{i}*{y}={i*y}", end=' ')

