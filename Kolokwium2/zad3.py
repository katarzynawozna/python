import math

class Ulamek:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik

    def skroc(self):
        nwd = math.gcd(self.licznik, self.mianownik)
        self.licznik //= nwd
        self.mianownik //= nwd
    
    def drukuj(self):
        print(f"({self.licznik} / ({self.mianownik}))")

    @staticmethod    
    def dodaj(ulamek1, ulamek2):
        lewy_licznik = ulamek1.licznik * ulamek2.mianownik
        prawy_licznik = ulamek2.licznik * ulamek1.mianownik
        dodawanie = Ulamek(lewy_licznik + prawy_licznik, ulamek1.mianownik * ulamek2.mianownik)
        dodawanie.skroc()
        return dodawanie
    
    @staticmethod
    def odejmij(ulamek1, ulamek2):
        lewy_licznik = ulamek1.licznik * ulamek2.mianownik
        prawy_licznik = ulamek2.licznik * ulamek1.mianownik
        odejmowanie = Ulamek(lewy_licznik - prawy_licznik, ulamek1.mianownik * ulamek2.mianownik)
        odejmowanie.skroc()
        return odejmowanie
    
    @staticmethod
    def mnoz(ulamek1, ulamek2):
        mnozenie = Ulamek(ulamek1.licznik * ulamek2.licznik, ulamek1.mianownik * ulamek2.mianownik)
        mnozenie.skorc()
        return mnozenie
    
    @staticmethod
    def dziel(ulamek1, ulamek2):
        dzielenie = Ulamek(ulamek1.licznik * ulamek2.mianownik, ulamek1.mianownik * ulamek2.licznik)
        dzielenie.skroc()
        return dzielenie

