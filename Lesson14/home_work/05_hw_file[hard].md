## "Обработка списка фруктов"

### Задание

Дана ведомость расчета заработной платы [data/workers.txt](data/workers.txt).

Рассчитайте зарплату всех работников, зная что они получат полный оклад, если отработают норму часов. \
Если же они отработали меньше нормы, то их ЗП уменьшается пропорционально, \
а за каждый час переработки они получают удвоенную ЗП, пропорциональную норме. \
Кол-во часов, которые были отработаны, указаны в файле ["data/hours_of.txt](data/hours_of.txt)

### Формат входных данных

Дано два текстовых файла. Один с информацией о сотрудниках, второй с количеством отработанных часов.

Гарантируется, что каждый сотрудник имеет уникальную фамилию(однофамильцев нет).

### Формат выходных данных

Выведите зарплату сотрудников с учетом переработки и недоработки.

### Решение задачи

def open_file_employees(in_file = "data/workers.txt"):
    employees = []
    with open(in_file, "r", encoding="UTF-8") as f:
        lines = [line.strip() for line in f]
        # print(lines)
        headers = lines[0].split()
        # print(headers)
        for line in lines[1:]:
            if line.strip():
                values = line.strip().split()
                employee = dict(zip(headers, values))
                employees.append(employee)
        # for emp in employees:
        #     print(emp)
    return employees



employees = open_file_employees()

employees_hours = open_file_employees("data/hours_of.txt")


result_lines = []
header = f"{'Фамилия':<15} {'Должность':<20} {'Реальная зарплата':>18}"
result_lines.append(header)

for employee_h in employees_hours:
    for employee in employees:
        if employee_h["Фамилия"] == employee["Фамилия"]:
            norm_hours = int(employee["Норма_часов"])
            worked_hours = int(employee_h["Отработано_часов"])
            salary = int(employee["Зарплата"])
            position = employee["Должность"]
            surname = employee["Фамилия"]

            hourly_rate = salary / norm_hours

            if worked_hours > norm_hours:
                overtime = worked_hours - norm_hours
                real_salary = salary + overtime * hourly_rate * 2
            elif worked_hours == norm_hours:
                real_salary = salary
            else:
                real_salary = worked_hours * hourly_rate

            result_line = f"{surname:<15} {position:<20} {real_salary:>18.2f}"
            result_lines.append(result_line)

for line in result_lines:
    print(line)
