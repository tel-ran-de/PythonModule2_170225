# Дан список словарей, где каждый словарь представляет собой информацию о человеке (например, {'name': 'Иван', 'age': 30}).
# Напишите функцию, которая возвращает список имен из этого списка.
def get_name(name):
    names = []
    for name in staff:
        names.append(name['name'])
    return names


staff = [
    {'name': 'Иван', 'age': 30},
    {'name': 'Ива', 'age': 39},
    {'name': 'Юра', 'age': 40},
    {'name': 'Федя', 'age': 32}
]
print(get_name(staff))
