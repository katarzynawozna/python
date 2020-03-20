def RepeatedWords(text):
    sentence = text.split()
    no_repetition = []
    for word in sentence:
        if word not in no_repetition:
            no_repetition.append(word)
    no_repetition = ' '.join(no_repetition)
    return no_repetition