import re

def ifURL(filename):
    with open(filename) as f:
        text = f.read()
    f.close()

    URLs = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    return URLs


    # można też po prostu przekazac funkcji stringa jako argument wtedy
# def ifURL(text):
    # URLs = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    # return URLs


