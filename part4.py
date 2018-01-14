import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys(),cutoff=0.8))>0:
        return "Did you mean %s instead?" %get_close_matches(word,data.keys(),cutoff=0.8)[0]
    else:
        return "Check the word again. It doesn't exist."

input_word = input("Enter the word: ")
print(translate(input_word.lower()))
