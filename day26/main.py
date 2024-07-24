import pandas


file = "nato_phonetic_alphabet.csv"
nato_alphabet = pandas.read_csv(file)
nato_alph_dict = {}

for index, row in nato_alphabet.iterrows():
    nato_alph_dict[row.letter] = row.code

word = input("Enter a word:").upper()
# result = []
# for letter in word:
#     if letter in nato_alph_dict:
#         result.append(nato_alph_dict[letter])

result = [nato_alph_dict[letter] for letter in word if letter in nato_alph_dict]

print(result)