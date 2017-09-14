import json
from difflib import get_close_matches

dictionnary = json.load(open("data.json", "r"))

def get_definition(word):
    word = word.lower()
    if word in dictionnary:
        print(dictionnary[word])
    else:

        possibleWords = get_close_matches(word, list(dictionnary.keys()))
        print("No word found")
        if len(possibleWords) > 0:
            print("You might meant:")
            print(possibleWords)
            

word = input("Please enter a word: ")
get_definition(word)
