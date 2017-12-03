'''
db{
name
surname
address
birth_date
gender
credit
phone_numb
}

'''
import shelve
import pprint
import datetime
from Client import *

def init():
    s = shelve.open('test_shelf.db')
    try:
        s['key1'] = { 'name': 'Roman', 'surname':'Bahlai', 'address':'Borshchiv', 'birth_date':datetime.date(1997,6,11),'gender':'male','credit': 1.1, 'phone_number':'+380666666666' }
        s['key2'] = { 'name': 'Taras', 'surname':'Shevchenko', 'address':'Morynci', 'birth_date':datetime.date(1814,3,9),'gender':'male','credit': 6.4, 'phone_number':'+380666666666' }
        s['key3'] = { 'name': 'Mishanya', 'surname':'Fasolyan', 'address':'Borshchiv', 'birth_date':datetime.date(1998,5,10),'gender':'male','credit': 13456.2, 'phone_number':'+380666666666' }
        s['key4'] = { 'name': 'Mishanya', 'surname':'Fasolyan', 'address':'Borshchiv', 'birth_date':datetime.date(1398,5,10),'gender':'male','credit': 100000.2, 'phone_number':'+380666666666' }
    finally:
        s.close()

def age_general(date):
        today = datetime.date.today()
        age = today.year - date.year
        if today < datetime.date(today.year, date.month, date.day):
            age -= 1
        return age

init()
def change_db():
    with shelve.open('test_shelf.db', writeback=True) as s:
        print('Initial data:')
        pprint.pprint(s['key1'])
        s['key1']['new_value'] = 'this was not here before'
        print('\nModified:')
        pprint.pprint(s['key1'])

with shelve.open('test_shelf.db', writeback=True) as s:
    for obj in s:
        print('\n')
        pprint.pprint(s[obj])

general_sum = 0
with shelve.open('test_shelf.db', writeback=True) as s:

    for obj in s:
        general_sum += float(s[obj]['credit'])
    print("-------------")
    print("Загальна сума кредитів = ", "%.2f" % general_sum, "UAH")
    
with shelve.open('test_shelf.db', writeback=True) as s:
    min_age = age_general(s['key1']['birth_date'])
    min_age_name = s['key1']['name'] + " "+s['key1']['surname']
    for obj in s:
        if min_age > age_general(s[obj]['birth_date']):
            min_age = age_general(s[obj]['birth_date'])
            min_age_name = s[obj]['name'] + " " + s[obj]['surname']
    print("Наймолодший кредитор -->", min_age,"y.o. -- "+ min_age_name)
    print("-------------")
           
      


