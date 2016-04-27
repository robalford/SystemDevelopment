import shelve
from add_book_data import AddressBook

d = shelve.open('book_data.shelve', 'n')

for person in AddressBook:
    #create a key
    key = '{} {}'.format(person[first_name], person[last_name])
    d[key] = person

d.close()

d2 = shelve.open('book_data.shelve')
