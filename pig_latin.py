"""To form Pig Latin, you take an English word that begins with a consonant, move that
consonant to the end, and then add “ay” to the end of the word. If the word begins with
a vowel, you simply add “way” to the end of the word."""

if __name__ == "__main__":
    print("Welcome to the pig latin generator!\n")
    input_word = input("Enter the word you want to change to Pig Latin: ")
    vowel_list = "aeiou"
    if input_word[0] in vowel_list:
        input_word = input_word + "way"
    else:
        input_word = input_word[1:] + input_word[0] + "ay"
    print(input_word)
