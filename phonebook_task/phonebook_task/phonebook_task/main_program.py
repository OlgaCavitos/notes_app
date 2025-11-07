from add_contact import add_contact
from find_contact import find_contact
from remove_contact import delete_contact
from update_contact import update_contact
from import_json import upload_phonebook

def options():
    while True:
        print("\nPhonebook Options:")
        print("1. Add new contact")
        print("2. Search by name")
        print("3. Search by phone number")
        print("4. Search by city")
        print("5. Update a record")
        print("6. Delete a record")
        print("7. Display all contacts")
        print("8. Exit")

        choice = input("Enter your choice 1-8: ")
        if choice == "1":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone_number = input("Enter phone number: ")
            city = input("Enter city: ")
            add_contact(first_name, last_name, phone_number, city)
            print("Contact added successfully")
        elif choice == "2":
            query = input("Enter search query: ")
            result=find_contact(query)
            print(result if result else "Not found")
        elif choice == "3":
            phone_number = input("Enter phone number: ")
            result=find_contact(phone_number)
            print(result if result else "Not found")
        elif choice == "4":
            city = input("Enter city: ")
            result=find_contact(city)
            print(result if result else "Not found")
        elif choice == "5":
            phone_number = input("Enter phone number: ")
            new_first_name = input("Enter new first name: ")
            new_last_name = input("Enter new last name: ")
            new_phone_number = input("Enter new phone number: ")
            new_city = input("Enter new city: ")
            update_contact(phone_number,new_first_name or None, new_last_name or None, new_phone_number or None, new_city or None)
            print("Contact updated successfully")
        elif choice == "6":
            phone_number = input("Enter phone number: ")
            delete_contact(phone_number)
            print("Contact deleted successfully")
        elif choice == "7":
            book = upload_phonebook()
            print(book["contacts"])
        elif choice == "8":
            print("Exit")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    options()





