import csv

with open('name.csv', 'w', newline='\n') as csvfile:
    fieldnames = ['first_name', 'last_name']

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    writer.writerow({'first_name': 'Bob', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Ali', 'last_name': 'Express'})
    writer.writerow({'first_name': 'Alice', 'last_name': 'Smith'})


with open('name.csv') as file:
    print(file.read())
