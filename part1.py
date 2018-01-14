import json
data = json.load(open("data.json"))

def translate(word):
    return data[word]

input_word = input("Enter the word: ")
print(translate(input_word))
