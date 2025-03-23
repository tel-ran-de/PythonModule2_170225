# Данные о сотрудниках в программе хранятся в словаре
staff = [
    {
        'name': 'Алексей',
        'surname': 'Петров',
        'salary': 124300
    },
    {
        'name': 'Николай',
        'surname': 'Петров',
        'salary': 120000
    },
    {
        'name': 'Иван',
        'surname': 'Павлов',
        'salary': 34500
    },
    {
        'name': 'Василий',
        'surname': 'Кукушкин',
        'salary': 162500
    },
    {
        'name': 'Василий',
        'surname': 'Павлов',
        'salary': 47800
    },
]
# Вычислите:
print("Имя и Фамилию сотрудника с самой высокой зарплатой:")
for key in staff:
    if key['salary'] == max(key['salary'] for key in staff):
        print((key['name'], key['surname']))
# TODO: your code here

print("Имя и Фамилию сотрудника с самой низкой зарплатой:")
for key in staff:
    if key['salary'] == min(key['salary'] for key in staff):
        print((key['name'], key['surname']))
# TODO: your code here

print("Среднеарифметическую зарплату всех сотрудников")

msalary = sum(key['salary'] for key in staff) / len(staff)
print(msalary)



# TODO: your code here

print("Количество однофамильцев в организации")
surname_count = {}
for person in staff:
    surname = person['surname']

    if surname not in surname_count:
     surname_count[surname] = 0

     surname_count[surname] += 1

    else:
     surname_count[surname] = 2

for surname, count in surname_count.items():
    print(f"{surname}: {count}")


# TODO: your code here

print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")
for i in range(len(staff)):
    for j in range(i + 1, len(staff)):
        if staff[i]['salary'] > staff[j]['salary']:
            staff[i], staff[j] = staff[j], staff[i]
for person in staff:
    print(person['name'], person['surname'])
# TODO: your code here
