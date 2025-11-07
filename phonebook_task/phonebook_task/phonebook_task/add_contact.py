from import_json import upload_phonebook,save_phonebook

def add_contact(first_name, last_name, phone_number,city):
    full_name = f"{first_name} {last_name}"
    book=upload_phonebook()
    contacts = [i for i in book["contacts"] if i["phone_number"].lower()!= phone_number.lower()]
    book["contacts"]=contacts
    save_phonebook(book)
    return book


