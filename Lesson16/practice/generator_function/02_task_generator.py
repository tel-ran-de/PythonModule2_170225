# Задача "Генератор обратного отсчета"
# Напишите генераторную функцию countdown(n), которая генерирует числа в обратном порядке от n до 1.

def countdown(n):
    for i in range(n):
        yield (n-i)


for num in countdown(10):
    print(num)
