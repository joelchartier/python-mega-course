def split(sentence = "Hello jojo"):

    words = []
    word = ""

    for character in sentence:
        if character == ' ':
            words.append(word)
            word = ""
        else:
            word += character

    words.append(word.upper())
    return words

print(split())
