# Дано текст. Потрібно:
# Порахувати частоту кожної літери (ігноруючи регістр).
# Визначити 3 найчастіші літери.
# Знайти всі унікальні слова.
# Вивести слова, що містять найбільше голосних.
text = "Програмування -- це цікава наука, яка змінює світ. Програмісти створюють нові технології."
vowels = {'а', 'е', 'є', 'и', 'і', 'ї', 'о', 'у', 'ю', 'я'}

text = text.lower().replace(",", "").replace(".", "").replace("--", "")
words = text.split()
print(f'{words=}')

letter_count = {char: text.count(char) for char in set(text) if char.isalpha()}
top_letters = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)[:3]
unique_words = set(words)

word_vowel_count = {word: sum(1 for char in word if char in vowels) for word in words}
max_vowel_words = [word for word, count in word_vowel_count.items() if count == max(word_vowel_count.values())]
print("Частота літер: ", letter_count)
print("ТОП-3 найчастіші літери: ", top_letters)
print("Унікальні слова: ", unique_words)
print("Слова з найбільшою к-сь голосних: ", max_vowel_words)