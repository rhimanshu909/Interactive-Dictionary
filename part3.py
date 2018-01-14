import json
data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    else:
        return "Check the word again. It doesn't exist."

input_word = input("Enter the word: ")
print(translate(input_word.lower()))
