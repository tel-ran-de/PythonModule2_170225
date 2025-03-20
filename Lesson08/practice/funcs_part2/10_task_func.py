# Напишите функцию, находящую среднее арифметическое всех аргументов
# Функция должна вызываться с любым количеством аргументов

def average(*args):
    if not args:  
        return "Нет данных"
    total = 0
    count = 0
    for num in args:
        total += num
        count += 1
    return round(total / count, 2)


print(average(3, 4, 8))
print(average(1, 4, 5, -3, 8, 4))
print(average(-10, 12, 6.3, -5.5, 7, 0.2))
