napis = input("Proszę coś napisać: ")

if napis[0] in napis:
    zamiana = napis.replace(napis[0], '$')
    nowy_napis = napis[0] + zamiana[1:]
    print(nowy_napis)
