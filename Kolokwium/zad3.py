zdanie = input("Podaj zdanie: ")

def panagram(zdanie):
    zdanie = zdanie.lower()
    zdanie = set(zdanie)
    sprawdzanie = [litera for litera in zdanie if ord(litera) in range(ord('a'), ord('z')+1)]

    if len(sprawdzanie) == 26:
        return "To jest panagram"
    else:
        return "To nie jest panagram"

print(panagram(zdanie))