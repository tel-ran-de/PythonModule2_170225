# Задача "Генератор обратного отсчета"
# Напишите генераторную функцию countdown(n), которая генерирует числа в обратном порядке от n до 1.

def countdown(n):
    for i in range(n, 0, -1):
        yield i


numer = countdown(10)

print(next(numer))
print(next(numer))
print(next(numer))
print(next(numer))
