# У вас есть список словарей, представляющих студентов с их именами и средними баллами.
# Вам нужно отфильтровать студентов, чей средний балл выше 4.5,
# и округлить средний балл оставшихся студентов до двух знаков после запятой.

students = [
    {'name': 'Alice', 'grade': 4.8},
    {'name': 'Bob', 'grade': 3.9},
    {'name': 'Charlie', 'grade': 4.65},
    {'name': 'David', 'grade': 4.2},
    {'name': 'Eve', 'grade': 4.91}
]
# Фильтр оценок > 4,5
students_note = list(filter(lambda student: student['grade'] > 4.5, students))
print(f"Студенты, чей средний балл выше 4.5 : {students_note}")

# Средний бал оставшихся оценок

students_not = list(filter(lambda student: student['grade'] < 4.5, students))

summa = sum(students_not['grade'] for students_not in students_not)
summa2 = summa / 2
print(f"Средний балл оставшихся студентов: {summa2:.2f}")
