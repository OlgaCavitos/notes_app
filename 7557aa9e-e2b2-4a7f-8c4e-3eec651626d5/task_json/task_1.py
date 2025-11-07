# Створіть функцію, яка зберігає дані про студентів (ім'я, вік, середній бал) у JSON-файл.
# Додайте можливість додати нового студента через введення даних користувачем.
import json

# Початкові дані
students = [
    {"name": "Олена", "age": 20, "average_grade": 4.5},
    {"name": "Іван", "age": 21, "average_grade": 4.8}
]


def add_student():
    name = input("Введіть ім'я студента: ")
    age = int(input("Введіть вік студента: "))
    grade = float(input("Введіть середній бал студента: "))

    new_studet = {"name": name, "age": age, "average_grade": grade}
    students.append(new_studet)
    with open("students.json", "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=4)


add_student()
