import pickle
from add_book_data import AddressBook

pickle.dump(AddressBook, open('book_data.pkl', 'wb'))
address_book = pickle.load(open('book_data.pkl', 'rb'))

print(address_book)