from import_json import upload_phonebook, save_phonebook

def update_contact(phone_number, new_first_name=None, new_last_name=None, new_phone_number=None, new_city=None):
    book = upload_phonebook()
    for i in book["contacts"]:
        if i["phone_number"].lower()== phone_number.lower():
            if new_first_name: i["first_name"]=new_first_name
            if new_last_name: i["last_name"]=new_last_name
            i["fullname"]=f"{i['first_name']}{i['last_name']}"
            if new_phone_number: i["phone_number"]=new_phone_number
            if new_city: i["city"]=new_city
            break
    save_phonebook(book)
    return book
