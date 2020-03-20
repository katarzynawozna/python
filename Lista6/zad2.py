import SzyfrCezara

napis = input("Podaj hasło do zakodowania(bez polskich znaków!): ")

print(SzyfrCezara.szyfrowanie(napis))
print(SzyfrCezara.odszyfrowywanie(SzyfrCezara.szyfrowanie(napis)))