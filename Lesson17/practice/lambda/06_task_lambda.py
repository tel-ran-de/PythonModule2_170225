# Дан готовый код
# def extract_name(person):
<<<<<<< HEAD
#  return person['name']


people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
# names = list(map(extract_name, people))
=======
#     return person['name']


people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
>>>>>>> 68b338dc43d0d6145b3c52e09c1e88e0928f2085
names = list(map(lambda person: person['name'], people))
print(names)

# Задача: перепишите код, используя lambda-функцию
