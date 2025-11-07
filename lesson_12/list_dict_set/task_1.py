# Дано список цілих чисел. Напишіть програму, яка "обертає" список на задану кількість позицій
# вправо за допомогою циклів. Наприклад, для списку [1, 2, 3, 4, 5] і обертання на 2 позиції
# результат буде [4, 5, 1, 2, 3].
lst = [1, 2, 3, 4, 5]
k = 2
n = len(lst)
new_lst = [0] * n
print('new_lst: ', new_lst)
for i in range(n):
    print('=' * 10)
    print("i + k: ", i + k)
    print("(i + k) % n: ", (i + k) % n)
    print('lst[i]: ', lst[i])
    new_lst[(i + k) % n] = lst[i]
    print('new_lst: ', new_lst)
print(new_lst)  # [4, 5, 1, 2, 3]