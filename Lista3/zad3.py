a = float(input("Proszę wprowadzić parametr 'a': "))
b = float(input("Proszę wprowadzić parametr 'b': "))
c = float(input("Proszę wprowadzić parametr 'c': "))

if a == 0:
	print("To nie będzie równanie kwadratowe!")
	a = float(input("Proszę wprowadzić inną liczbę: "))

delta = b**2 - 4*a*c

if delta > 0:
	x1 = -b-(delta**(1/2))/2*a
	x2 = -b+(delta**(1/2))/2*a
	print("Pierwiastki tego równania to: " + str(x1) + " i " + str(x2))
elif delta == 0:
	x1 = -b/2*a
	print("Pierwiastek tego równania to: " + str(x1))
else:
	print("To równanie nie ma pierwiastków!")
	
