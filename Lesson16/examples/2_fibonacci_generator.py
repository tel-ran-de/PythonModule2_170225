def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for num in fibonacci(10):
    print(num)  # Выведет первые 10 чисел Фибоначчи

# Генератор fibonacci генерирует числа Фибоначчи по запросу, не храня всю последовательность в памяти

squares_generator = (x**2 for x in range(1, 6))

# squares_generator - это объект-генератор
print(squares_generator)  # Выведет: <generator object <genexpr> at 0x...>

for square in squares_generator:
    print(square)  # Выведет: 1, 4, 9, 16, 25


squares = [x**2 for x in range(1, 6)]
print(squares)  # Выведет: [1, 4, 9, 16, 25]

for square in squares_generator:
    print(square)  # Выведет: 1, 4, 9, 16, 25

sum_of_squares = sum(x**2 for x in range(1, 11))
print(sum_of_squares)  # Выведет: 385