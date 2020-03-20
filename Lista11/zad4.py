import re

def startswithA_E(text):
    words = re.findall(r'\b[aAeE]\w+', text)
    return words