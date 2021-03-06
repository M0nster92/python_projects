import json

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "this word doesn't exist"

word = input("Enter Word: ")

print(translate(word))