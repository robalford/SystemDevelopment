import json
from add_book_data import AddressBook

with open('book_data.json', 'w') as f:
    json.dump(AddressBook, f)

with open('book_data.json', 'r') as f:
    address_book = json.load(f)

print(address_book)