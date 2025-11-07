from module_1 import count_words
from module_2 import count_letters
text = "How many words and letters in the text?"

# count_words function from module_1
word_count = count_words(text)
print(f"Number of words: {word_count}")

#count_letters function from module_2
letter_count = count_letters(text)
print(f"Number of letters: {letter_count}")
