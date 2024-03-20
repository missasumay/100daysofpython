from pandas import *

data = read_csv("day26\\nato_alphabet\\nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter:row.code for (index, row) in data.iterrows()}

name = input("Type a word: ").upper()

name_coded = [nato_alphabet[letter] for letter in name]

print(name_coded)

