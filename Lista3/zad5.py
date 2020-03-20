import re

hasło = input("Proszę podać swoje hasło: ")
x = True
while x:
    if (len(hasło)>16 or len(hasło)<6):
        break
    elif not re.search("[a-z]", hasło):
        break
    elif not re.search("[A-Z]", hasło):
        break
    elif not re.search("[0-9]", hasło):
        break
    elif not re.search("[$#@]", hasło):
        break
    else:
        print("Hasło poprawne!")
        x = False
        break
if x:
    print("Hasło niepoprawne!")
