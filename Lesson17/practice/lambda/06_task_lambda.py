# Дан готовый код
def extract_name(person):
    return person['name']


people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
names = list(map(extract_name, people))
print(names)

# Задача: перепишите код, используя lambda-функцию
