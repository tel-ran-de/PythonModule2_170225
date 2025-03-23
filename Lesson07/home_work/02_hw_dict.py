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
max_salary = 0
min_salary = 0
highest_paid = {}
surname_count = {}
sorted_staff = {}

print("Имя и Фамилию сотрудника с самой высокой зарплатой:")
for item in staff:
    if item['salary'] > max_salary:
        max_salary = item['salary']
        highest_paid = item
print(f"Максимальная зарплата: = {highest_paid['salary']} >>> {highest_paid['name']} {highest_paid['surname']} ")
print("--------------------\n")

print("Имя и Фамилию сотрудника с самой низкой зарплатой:")
for item in staff:
    if item['salary'] < max_salary:
        min_salary = item['salary']
        highest_paid = item
print(f"Минимальная зарплата: = {highest_paid['salary']} >>> {highest_paid['name']} {highest_paid['surname']} ")
print("--------------------\n")

print("Среднеарифметическую зарплату всех сотрудников")
# average_salary = sum(item['salary'] for item in staff) / len(staff)
print(f"Средняя зарплата по палате: = {sum(item['salary'] for item in staff) / len(staff):.2f} ")
print("--------------------\n")

print("Количество однофамильцев в организации")
for item in staff:
    surname = item['surname']
    if surname in surname_count:
        surname_count[surname] += 1
    else:
        surname_count[surname] = 1
print(f"{surname_count}")
for surname, count in surname_count.items():
    if count > 1:
        print(f"Однофамильцы в организации {surname}: {count} человека/человек")
print("--------------------\n")

print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")
sorted_staff = sorted(staff, key=lambda x: x["salary"], reverse=True)
for employee in sorted_staff:
    print(employee["name"], employee["surname"], employee["salary"])
