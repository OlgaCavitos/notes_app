import json

FILE_NAME = "path to file"


def read_from_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        pass


def save_data(my_book, FILE_NAME):
    pass


def add(my_book):
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    phone_number = input("Enter your phone_number: ")
    city = input("Enter your city: ")
    my_book[f"{first_name} {last_name}"] = {"number": phone_number, "city": city}
    return my_book


def search_by_first_name(item, my_book):
    search_result = []
    for key in my_book.keys():
        if key.startwith(item):
            search_result.append(item)
    return search_result


def search_city(item, my_book):
    for key, value in my_book.items():
        if value["city"] == item:
            return key
        print('Not found...')
    return None
