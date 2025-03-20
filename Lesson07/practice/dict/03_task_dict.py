# Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом,
# чтобы элементы первого списка были ключами, а элементы второго — соответственно значениями нашего словаря.

keys = ['name', 'surname', 'age', 'rate']
values = ['Петр', 'Первый', 42, 1300]

<<<<<<< HEAD



Dict = {
    keys[0]: values[0] ,
    keys[1]:  values[1],
    keys[2]:  values[2],
    keys[3]:  values[3]

}

print(Dict)

# TODO: your code here
=======
people = dict(zip(keys, values))

# people = {}
# for i in range(len(keys)):
#     key = keys[i]
#     value = values[i]
#     people[key] = value
#
print(people)

>>>>>>> 154385c3b5f72787a35f27bb8b6927527704f159
# Нужно получить словарь:
# {'name': 'Петр', 'surname': 'Первый', 'age': 42, 'rate': 1300}
