napis = input("Proszę coś napisać: ")
x = int(len(napis)/2)
napis_w_srodku = napis[:x] + 'PSIKUS' + napis[x:]
print(napis_w_srodku)