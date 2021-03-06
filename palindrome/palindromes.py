"""Find palindromes (letter palingrams) in a dictionary file."""

import load_dictionary

word_list = load_dictionary.load("dictionary.txt")
pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print(f"\nNumber of Palindromes found = {len(pali_list)}\n")
print(*pali_list, sep = "\n")

