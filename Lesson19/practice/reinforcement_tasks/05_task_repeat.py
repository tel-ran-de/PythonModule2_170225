# "Наивысшая оценка"
#
# Дан список кортежей, где каждый кортеж представляет собой пару (имя, оценка).
# Необходимо найти имя с наивысшей оценкой.
# Если наивысших оценок несколько, вывести имена

students = [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('David', 92)]
# Ожидаемый результат: 'Bob' и 'David

students.sort(key=lambda student: student[1], reverse=True)
max(students, key=lambda student: student[1])

max_points = students[0][1]

for student in students:
    if student[1] == max_points:
        print(student)
