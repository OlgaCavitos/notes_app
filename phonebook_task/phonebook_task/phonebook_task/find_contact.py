from import_json import upload_phonebook

def find_contact(term):
    book = upload_phonebook()
    term = term.lower()
    result=[
        i for i in book["contacts"]
        if term in i.get("first_name", "").lower()
        or term in i.get("last_name", "").lower()
        or term in i.get("full_name", "").lower()
        or term in i.get("phone_number", "").lower()
        or term in i.get("city", "").lower()]
    return result