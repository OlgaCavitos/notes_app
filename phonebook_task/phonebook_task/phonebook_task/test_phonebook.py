import unittest
import tempfile
import os
import json


import import_json
from add_contact import add_contact
from find_contact import find_contact
from update_contact import update_contact
from remove_contact import delete_contact

# test data
sample_data = {
    "contacts": [
        {
            "first_name": "Neil",
            "last_name": "Hoking",
            "full_name": "Neil Hoking",
            "phone_number": "653458",
            "city": "Seattle"
        },
        {
            "first_name": "Mila",
            "last_name": "Candy",
            "full_name": "Mila Candy",
            "phone_number": "054321",
            "city": "Portland"
        }
    ]
}

class TestPhonebook(unittest.TestCase):

    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+', encoding='utf-8')
        json.dump(sample_data, self.temp_file, ensure_ascii=False, indent=4)
        self.temp_file.close()


        import_json.FILE = self.temp_file.name

    def tearDown(self):
        os.remove(self.temp_file.name)

    def test_upload_phonebook(self):
        book = import_json.upload_phonebook()
        self.assertEqual(len(book['contacts']), 2)

    def test_add_contact(self):
        add_contact("Lory", "Johnson", "654321", "Chicago")
        book = import_json.upload_phonebook()
        numbers = [c['phone_number'] for c in book['contacts']]
        self.assertIn("654321", numbers)

    def test_find_contact_by_name(self):
        result = find_contact("Neil")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["city"], "Seattle")

    def test_find_contact_by_city(self):
        result = find_contact("Portland")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["first_name"], "Mila")

    def test_update_contact(self):
        update_contact("653458", new_first_name="Tom", new_city="Brain")
        book = import_json.upload_phonebook()
        contact = next(c for c in book['contacts'] if c['phone_number'] == "653458")
        self.assertEqual(contact["first_name"], "Tom")
        self.assertEqual(contact["city"], "Boston")

    def test_delete_contact(self):
        delete_contact("054321")
        book = import_json.upload_phonebook()
        numbers = [c["phone_number"] for c in book["contacts"]]
        self.assertNotIn("054321", numbers)


if __name__ == '__main__':
    unittest.main()