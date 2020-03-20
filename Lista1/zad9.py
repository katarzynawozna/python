import cmath
z = complex(input())
modul_z = cmath.sqrt((z.real)**2 + (z.imag)**2)
argument = cmath.phase(z)
z.conjugate()
