# with open('Weekdays.txt','r') as week_file:
#     weekdays = [day.rstrip() for day in week_file.readlines()]
# print(weekdays)
#

# se1=("168","192","92","91")
# print("-".join(se1))
# print(".".join(se1))
# print(",".join(se1))










def options():
    print("1. Add new entries")
    print("2. Search by first_name")
    print("3. Search by last_name")
    print("4. Search by full_name")
    print("5. Search by telephone_number")
    print("6. Search by city or state")
    print("7. Delete a record for a given telephone number")
    print("8. Update a record for a given telephone number")
    print("9. Remove a record for a given telephone number")

    choice_option = int(input("Please enter your choice: "))
    return choice_option







# def phone_book(name, *args):
#     return name + ", " + ", ".join(args)
# def add_number():
