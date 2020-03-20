import numpy as np
import matplotlib.pyplot as plt

# https://pl.wikipedia.org/wiki/Rzut_uko%C5%9Bny_(fizyka) --> źródło wzorów


przyspieszenie_ziemskie = 9.80665  # [m / s^2] 

def h_max(predkosc_v0, kat):
	return (predkosc_v0 * np.sin(kat)) ** 2 / (2 * przyspieszenie_ziemskie)

def zasieg(predkosc_v0, kat):
	return predkosc_v0 ** 2  * np.sin(2 * kat) / przyspieszenie_ziemskie

def czas_lotu(predkosc_v0, kat):
	return 2 * predkosc_v0 * np.sin(kat) / przyspieszenie_ziemskie

def predkosc_chwilowaVY(predkosc_v0, kat, t):
	return max(0, predkosc_v0 * np.sin(kat) - przyspieszenie_ziemskie * t)
	# ans = predkosc_v0 * np.sin(kat) - przyspieszenie_ziemskie * t
	# # Zakładamy, że prędkość nie może być poniżej 0 (czyli nie spada pod ziemię)
	# if ans > 0:
	# 	return ans
	# else:
	# 	return 0

# Zawsze jest stała, więc nie wymaga czasu t
def predkosc_chwilowaVX(predkosc_v0, kat):
	return predkosc_v0 * np.cos(kat)

def polozenie_x(predkosc_v0, kat, t):
	return predkosc_v0 * np.cos(kat) * t

def polozenie_y(predkosc_v0, kat, t):
	return predkosc_v0 * np.sin(kat) * t - przyspieszenie_ziemskie * t ** 2 / 2


if __name__ == '__main__':
	while True:
		predkosc_v0 = input('Podaj prędkość początkową [m/s]: ')
		try:
			predkosc_v0 = float(predkosc_v0)
			break
		except ValueError:
			print('Podana wartość nie mogła zostać zinterpretowana jako liczba. Spróbuj ponownie.')

	while True:
		kat = input('Podaj kąt rzutu [rad]: ')
		try:
			kat = float(kat)
			break
		except ValueError:
			print('Podana wartość nie mogła zostać zinterpretowana jako liczba. Spróbuj ponownie.')

	print(f"Ciało wzniesię się maksymalnie na {h_max(predkosc_v0, kat)}[m].")
	print(f"Zasięg rzutu wyniesie {zasieg(predkosc_v0, kat)}[m].")
	print(f"Czas lotu wyniesie {czas_lotu(predkosc_v0, kat)}[s].")

	### 4. Wykres prędkości chwilowej w kierunku pionowym i poziomym po czasie t ###
	ts = np.linspace(0, 10)  
	v_vertical = [predkosc_chwilowaVX(predkosc_v0, kat) for t in ts]  # Wszędzie jest ta sama wartość, ale wciąż potrzebujemy tych punktów, żeby je narysować
	v_horizontal = [predkosc_chwilowaVY(predkosc_v0, kat, t) for t in ts]

	plt.subplot(1, 3, 1)  
	plt.plot(ts, v_vertical, label="Pr. poziomo")
	plt.plot(ts, v_horizontal, label="Pr. pionowo")
	plt.title("Prędkość")
	plt.legend()

	### 5. Wykres położenia od czasu ###
	x = [polozenie_x(predkosc_v0, kat, t) for t in ts]
	y = [polozenie_y(predkosc_v0, kat, t) for t in ts]

	plt.subplot(1, 3, 2)
	plt.plot(ts, x, label="Poł. poziomo")
	plt.plot(ts, y, label="Poł. pionowo")
	plt.title("Położenie")
	plt.legend()

	### 6. Wykres toru rzutu ukośnego (czyli po prostu wykres położenia x od położenia y) ###
	plt.subplot(1, 3, 3)
	plt.plot(x, y)
	plt.title("Tor rzutu ukośnego")
	plt.show() 
