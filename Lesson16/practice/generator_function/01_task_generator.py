# Задача "Генератор четных чисел"
# Напишите генераторную функцию even_numbers(n), которая генерирует все четные числа от 0 до n включительно.

def even_numbers(n):
<<<<<<< HEAD
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


even = even_numbers(10)

print(next(even))
print(next(even))
print(next(even))
print(next(even))
=======
    for number in range(0, n + 1, 2):
        yield number


for el in even_numbers(11):
    print(el)
>>>>>>> d6041d05ecef6a9912aa912e92a67475e5be03d6
