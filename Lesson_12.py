## Дано список цілих чисел. Напишіть програму, яка "обертає" список на задану кількість позицій
# вправо за допомогою циклів. Наприклад, для списку [1, 2, 3, 4, 5] і обертання на 2 позиції
# результат буде [4, 5, 1, 2, 3]

# lst_1=[1, 2, 3, 4, 5, 6, 7]
# new_lst=[0]*len(lst_1)
# key_1=2
# for i in range(len(lst_1)):
#     print(f"index {i}")
#     print(f"new index={(i+key_1)%len(lst_1)}")
#     new_lst[(i+key_1)%len(lst_1)]=lst_1[i]
#     print(f"new_lst={new_lst}")
# print("Result:")
# print(new_lst)


## Дано список рядків. Використовуючи сет, знайдіть і виведіть усі унікальні символи, які
# зустрічаються в усіх рядках разом, а потім порахуйте, скільки разів кожен із них з’являється
# загалом.
#lst = ["hello", "world", "python"]
# {'h', 'e', 'l', 'o', 'w', 'r', 'd', 'p', 'y', 't', 'n'}
# {'h': 2, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1, 'p': 1, 'y': 1, 't': 1, 'n': 1}

# lst = ["hello", "world", "python"]
# unique_chars=set()
# #print(unique_chars)
# for i in lst:
#     for char in i:
#         unique_chars.add(char)
#
# print(unique_chars)
# #new_lst = lst[:]
#
# counts=dict()
#


# for char in unique_chars:
#     total_count=0
#
#     for i in lst:
#         for c in i:
#             if c==char:
#                 total_count+=1
#     counts[char]=total_count
#
# print(counts)

# lst = ["hello", "world", "python"]
# counts = dict()
#
# new_str = ""
#
# for i in lst:
#     new_str += i
#
# unic_chars = set(new_str)
#
# for i in unic_chars:
#     counts[i] = new_str.count(i)
# print(counts)

# lst = ["hello", "world", "python"]
# from collections import Counter
# unic_chars={ch for s in lst for ch in s}
# counts=Counter("".join(lst))
# print(unic_chars)
# print(dict(counts))

# Дано два словники, де ключі - це рядки, а значення - цілі числа. Створіть новий словник, який
# міститиме лише ті пари ключ-значення, де ключ присутній в обох словниках, а значення - це
# сума значень із двох словників.
# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 4, "c": 5, "d": 6}
#
#
# new_dict={}
# for key in dict1:
#     if key in dict2:
#         new_dict[key]=dict1[key] + dict2[key]
#
# print(new_dict)


# text="Exceptional text"
# vowels={'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
#
# text=text.lower().replace('?','').replace('!','').replace('.','')
#
# words=text.split()
# print(f'{words}')



# # Початкові дані
# import json
#
# students = [
#     {"name": "Олена", "age": 20, "average_grade": 4.5},
#     {"name": "Іван", "age": 21, "average_grade": 4.8}
# ]
#
# def add_student():
#     name=input("Please add the student name: ")
#     age=int(input("Please add the student age: "))
#     average_grade=float(input("Please add the student average grade: "))
#
#     new_studet={"name": name, "age":age ,"average_grade": average_grade}
#     students.append(new_studet)
#     with open("student.json", "w", encoding="utf-8") as f:
#         json.dump(students, f, ensure_ascii=False, indent=4)
#
# add_student()



# import csv
#
# with open('name.csv','w',newline='\n') as csvfile:
#     fieldnames=['first name', 'last name']
#     writer=csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#
#     writer.writerow({'first name': 'Olivia', 'last name': 'Beans'})
#     writer.writerow({'first name': 'Olena', 'last name': 'Bird'})
#
# with open('name.csv') as file:
#     print(file.read())


import csv

def save_students_to_csv(filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Average grade"])

        while True:
            name=input("Enter student name or 'stop' for finishing: ")
            if name.lower()=='stop':
                break
            age=input('Enter student age: ')
            grade=input('Enter student grade: ')
            writer.writerow([name, age, grade])

save_students_to_csv('students.csv')
print('Data is saved')