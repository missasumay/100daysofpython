from pandas import *

data = read_csv("day26\\nato_alphabet\\nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter:row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    name = input("Type a word: ").upper()

    try:
        name_coded = [nato_alphabet[letter] for letter in name]

    except KeyError: 
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()

    else:
        print(name_coded)

generate_phonetic()
