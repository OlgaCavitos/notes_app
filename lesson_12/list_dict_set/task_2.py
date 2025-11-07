# Дано список рядків. Використовуючи сет, знайдіть і виведіть усі унікальні символи, які
# зустрічаються в усіх рядках разом, а потім порахуйте, скільки разів кожен із них з’являється
# загалом.
lst = ["hello", "world", "python"]
# {'h', 'e', 'l', 'o', 'w', 'r', 'd', 'p', 'y', 't', 'n'}
# {'h': 2, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1, 'p': 1, 'y': 1, 't': 1, 'n': 1}

unique_chars = set()
for s in lst:
    for char in s:
        unique_chars.add(char)
counts = {}
for char in unique_chars:
    total = 0
    for s in lst:
        for c in s:
            if c == char:
                total += 1
    counts[char] = total

print(unique_chars)
print(counts)


# from collections import Counter
# unique_chars = {ch for s in lst for ch in s}
# counts = Counter("".join(lst))
#
# print(unique_chars)
# print(dict(counts))
