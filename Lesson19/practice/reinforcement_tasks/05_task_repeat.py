# "Наивысшая оценка"
#
# Дан список кортежей, где каждый кортеж представляет собой пару (имя, оценка).
# Необходимо найти имя с наивысшей оценкой.
# Если наивысших оценок несколько, вывести имена

students = [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('David', 92)]
max_points = max(students, key=lambda x: x[1])[1]

for student in students:
    if student[1] == max_points:
        print(student)