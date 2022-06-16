import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")


new_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(new_dict)

word = input("Enter your name: ").upper()

new_list = [new_dict[letter] for letter in word]
print(new_list)