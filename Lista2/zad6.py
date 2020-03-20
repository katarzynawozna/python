lista_studentów = ['Kasia', 'Basia', 'Marek', 'Darek']
lista_studentów.append('Józek')
lista_studentów.extend(['Ania', 'Basia'])
lista_studentów.sort()

print(lista_studentów[3])
print(lista_studentów[:2])
print(lista_studentów[-2:])

for Basia in range(0, len(lista_studentów)):
    if 'Basia' in lista_studentów:
        lista_studentów.remove('Basia')
    
len(lista_studentów)
lista_studentów = tuple(lista_studentów)
print(type(lista_studentów))