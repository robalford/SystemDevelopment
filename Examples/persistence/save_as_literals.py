import ast
from add_book_data import AddressBook

s = repr(AddressBook)
with open('book_data.txt', 'w') as f:
    f.write(s)
with open('book_data.txt', 'r') as f:
    s = f.read()
address_book = ast.literal_eval(s)
print(s)