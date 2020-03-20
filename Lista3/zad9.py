m_kolumny = int(input("Podaj liczbę kolumn tabeli: "))
n_wiersze = int(input("Podaj liczbę wierszy tabeli: "))


tabela = [[ 0 for x in range(m_kolumny)]  for y in range(n_wiersze)]

for i in range(0, m_kolumny):
    for j  in range(0, n_wiersze):
        tabela[0][i] = i
        tabela[j][0] = j
        tabela[j][i] = j*i
    
for wiersze in tabela:
    print(wiersze)



