from module_1 import count_words

def count_letters(text):
    #Counts the number of letters
    letters = [char for char in text if char.isalpha()]
    return len(letters)
