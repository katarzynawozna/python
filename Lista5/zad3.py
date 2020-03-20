def rzym_na_arab(str):
    rzym = {'I':1 , 'V':5 , 'X':10 , 'L':50 , 'C':100 , 'D':500 , 'M':1000}
    arabskie = 0
    for i in range(len(str)):
        wartosc_rzym = rzym[str[i]]
        if i+1 < len(str) and rzym[str[i+1]] > wartosc_rzym:
        #sprawdzanie czy na następnym miejscu jest litera przyjemująca większą wartość, co oznaczałoby odejmowanie obecnej od nastepnej - IV = -1 + 5 = 4;
            arabskie -= wartosc_rzym
        else:
            arabskie += wartosc_rzym
    return arabskie