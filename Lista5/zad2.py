def liczba_na_slowo(number):
    jednosci = {
        0 : '',
        1: 'jeden',
        2: 'dwa',
        3: 'trzy',
        4: 'cztery',
        5: 'pięć',
        6: 'sześć',
        7: 'siedem',
        8: 'osiem',
        9: 'dziewięć',
    }

    nastki = {
        10: 'dziesięć',
        11: 'jedenaście',
        12: 'dwanaście',
        13: 'trzynaście',
        14: 'czternaście',
        15: 'piętnaście',
        16: 'szesnaście',
        17: 'siedemnaście',
        18: 'osiemnaście',
        19: 'dziewiętnaście'
    }

    dziesiatki = {
        0 : '',
        1: 'dziesięć',
        2: 'dwadzieścia',
        3: 'trzydzieści',
        4: 'czterdzieści',
        5: 'pięćdziesiąt',
        6: 'sześćdziesiąt',
        7: 'siedemdziesiąt',
        8: 'osiemdziesiąt',
        9: 'dziewięćdziesiąt',
    }
    setki = {
        0 : '',
        1: 'sto',
        2: 'dwieście',
        3: 'trzysta',
        4: 'czterysta',
        5: 'pięćset',
        6: 'sześćset',
        7: 'siedemset',
        8: 'osiemset',
        9: 'dziewięćset',
    }

    tysiace = {1: 'tysiac'}

    if len(str(number)) == 4:
        tysiac, setka, dziesiatka, jednosc = [int(letter) for letter in str(number)]
        if dziesiatka == 1:
            nascie = str(dziesiatka) + str(jednosc)
            slownie = tysiace[tysiac] + ' ' + setki[setka]+ ' ' + nastki[int(nascie)]
            return slownie
        else:
            slownie = tysiace[tysiac] + ' ' + setki[setka] + ' ' + dziesiatki[dziesiatka] + ' ' + jednosci[jednosc]
            return slownie 
    elif len(str(number)) == 3:
        setka, dziesiatka, jednosc = [int(letter) for letter in str(number)]
        if dziesiatka == 1:
            nascie = str(dziesiatka) + str(jednosc)
            slownie = setki[setka]+ ' ' + nastki[int(nascie)]
            return slownie
        else:
            slownie = setki[setka] + ' ' + dziesiatki[dziesiatka] + ' ' + jednosci[jednosc]
            return slownie 
    elif len(str(number)) == 2:
        nascie = [int(letter) for letter in str(number)]
        nascie = ''.join(str(x) for x in nascie)
        slownie = nastki[int(nascie)]
        return slownie
    elif len(str(number)) == 1:
        slownie = jednosci[number]
    return slownie