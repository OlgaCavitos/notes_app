# Створіть програму, яка записує дані про студентів (ім'я, вік, середній бал) у CSV-файл.
# Дані вводяться користувачем, поки він не введе "stop".

import csv

def save_students_to_csv(filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Age', 'Average grade'])

        while True:
            name = input("Enter student name or 'stop' for finishing: ")
            if name.lower() == 'stop':
                break
            age = input('Enter student age: ')
            grade = input('Enter student average grade: ')
            writer.writerow([name, age, grade])

save_students_to_csv('students.csv')
print('Data is saved...')