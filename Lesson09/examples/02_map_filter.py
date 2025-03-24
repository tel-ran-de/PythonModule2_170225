# Пример использования функции map()
# map() применяет функцию к каждому элементу итерируемого объекта

def square(x):
  """Возвращает квадрат числа."""
  return x ** 2

numbers = [1, 2, 3, 4, 5]

# Применяем функцию square() к каждому элементу списка numbers
squared_numbers = list(map(square, numbers))

print(squared_numbers)  # Вывод: [1, 4, 9, 16, 25]

# Пример использования функции filter()
# filter() фильтрует элементы итерируемого объекта на основе функции-предиката

def is_even(x):
  """Возвращает True, если число четное, иначе False."""
  return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]

# Фильтруем список numbers, оставляя только четные числа
even_numbers = list(filter(is_even, numbers))

print(even_numbers)  # Вывод: [2, 4, 6]

# Пример использования функции reduce()
# reduce() применяет функцию к элементам итерируемого объекта накопительно

from functools import reduce

def multiply(x, y):
  """Возвращает произведение двух чисел."""
  return x * y

numbers = [1, 2, 3, 4, 5]

# Находим произведение всех элементов списка numbers
product = reduce(multiply, numbers)

print(product)  # Вывод: 120

# Пример использования лямбда-функции с map()
# Лямбда-функции - это анонимные функции, которые можно создавать "на лету"

numbers = [1, 2, 3, 4, 5]

# Используем лямбда-функцию для возведения каждого числа в квадрат
squared_numbers = list(map(lambda x: x ** 2, numbers))

print(squared_numbers)  # Вывод: [1, 4, 9, 16, 25]

# Пример использования лямбда-функции с filter()

numbers = [1, 2, 3, 4, 5, 6]

# Используем лямбда-функцию для фильтрации только четных чисел
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # Вывод: [2, 4, 6]

# Пример использования лямбда-функции с reduce()

numbers = [1, 2, 3, 4, 5]

# Используем лямбда-функцию для нахождения произведения всех чисел
product = reduce(lambda x, y: x * y, numbers)

print(product)  # Вывод: 120