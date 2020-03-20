def srednia_arytmetyczna(*args):
        srednia = []
        for i in args:
            srednia.append(i)
        if sum(srednia) != 0:
            srednia = sum(srednia)/len(srednia)
            return srednia
        else:
            return 0