import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys(),cutoff=0.8))>0:
        response = input("Did you mean %s instead? Enter Y if yes, or N if no: " %get_close_matches(word,data.keys(),cutoff=0.8)[0])
        if response == 'Y' or response == 'y':
            return data[get_close_matches(word,data.keys(),cutoff=0.8)[0]]
        elif response == 'N' or response == 'n':
            return "Check the word again. It doesn't exist."
        else:
            return "You didn't enter Y/y or N/n."
    else:
        return "Check the word again. It doesn't exist."

input_word = input("Enter the word: ")
if input_word[0].isupper() is True:
    output = translate(input_word)
else:
    output = translate(input_word.lower())
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
