import re

def space_between(text):
    with_spaces = re.sub(r"(\w)([A-Z])", r"\1 \2", text)
    return with_spaces