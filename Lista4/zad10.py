def NWD(a,b):
    reszta = a % b
    if reszta == 0:
        return b
    else:
        while reszta != 0:
            a = b
            b = reszta
            reszta = a % b
        if reszta == 0:
            return b

