"""
    First Application from Python-Mega-Course
"""

import json
from difflib import get_close_matches

DATA = json.load(open("data.json", "r"))

def run():
    """ Execute the application """
    user_input = input("Please enter a word: ").lower()

    if user_input in DATA:
        print("Here are the found definition(s) for the word [%s]" % user_input)
        for index, definition in enumerate(DATA[user_input]):
            print("%s) %s" % (index + 1, definition))
        return

    possible_words = get_close_matches(user_input, DATA.keys(), cutoff=0.8)
    if possible_words:
        print("You might meant: %s" % possible_words)
        run()
    else:
        print("No word found")

run()
