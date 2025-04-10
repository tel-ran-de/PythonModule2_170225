# Пример 1: Лямбда-функция для возведения числа в квадрат
square = lambda x: x**2
print(square(5))  # Вывод: 25

# Пример 2: Лямбда-функция для сложения двух чисел
add = lambda a, b: a + b
print(add(3, 7))  # Вывод: 10

# Пример 3: Использование lambda с map() для возведения в квадрат каждого элемента списка
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Вывод: [1, 4, 9, 16, 25]

# Пример 4: Использование lambda с filter() для фильтрации четных чисел из списка
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Вывод: [2, 4]