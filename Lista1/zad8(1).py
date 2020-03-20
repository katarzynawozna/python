a = int(input())
b = int(input())
if b < a:
	Z = b%a
	Z *= Z+3
	print(Z)
else:
	print("b musi być mniejsze od a!")
