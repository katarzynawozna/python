def silnia(n):
    silnia = 1
    x = 1
    while x in range(1, int(n)+1):
        silnia *= x
        x += 1
    return silnia