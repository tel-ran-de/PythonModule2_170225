# Дан список словарей, где каждый словарь представляет собой информацию о человеке (имя, возраст).
# Напишите функцию, которая возвращает новый список, содержащий только те словари, где возраст человека больше 18.
from idlelib.parenmatch import ParenMatch
from tkinter.font import names

lis = [

    { "name": "Peter", "age" : 18},
    { "name": "John", "age" : 15},
    { "name": "Anna", "age" : 19},
    { "name": "Kate", "age" : 22}

]

def select_age(lis):
    new_lis = []
    for i in lis:
        if i['age'] > 18:
            new_lis.append(i)
            print(new_lis)
    return

filtred_list = select_age(lis)
print(filtred_list)

