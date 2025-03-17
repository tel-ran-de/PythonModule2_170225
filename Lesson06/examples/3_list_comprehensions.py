# List comprehensions(списковые включения) - это компактный способ создания списков,
# позволяющий применять выражения к элементам итерируемых объектов.

# Пример 1: Создание списка квадратов чисел от 0 до 9.
squares = [x**2 for x in range(10)]
# Эквивалентно:
# squares = []
# for x in range(10):
#     squares.append(x**2)
print(squares) # Вывод: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Пример 2: Создание списка четных чисел из другого списка.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
# Эквивалентно:
# even_numbers = []
# for x in numbers:
#     if x % 2 == 0:
#         even_numbers.append(x)
print(even_numbers) # Вывод: [2, 4, 6, 8, 10]

# Пример 3: Создание списка слов, начинающихся с буквы 'a', из строки.
text = "apple banana apricot cherry avocado"
words = text.split() # Разбиваем строку на список слов.
a_words = [word for word in words if word.startswith('a')]
# Эквивалентно:
# a_words = []
# for word in words:
#     if word.startswith('a'):
#         a_words.append(word)
print(a_words) # Вывод: ['apple', 'apricot', 'avocado']

# Пример 4: Создание списка кортежей, содержащих (число, квадрат числа).
pairs = [(x, x**2) for x in range(5)]
# Эквивалентно:
# pairs = []
# for x in range(5):
#     pairs.append((x, x**2))
print(pairs) # Вывод: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]

# Пример 5: Создание списка букв из строки, исключая гласные.
vowels = "aeiou"
text = "hello world"
consonants = [char for char in text if char not in vowels and char != " "]
# Эквивалентно:
# consonants = []
# for char in text:
#     if char not in vowels and char != " ":
#         consonants.append(char)
print(consonants) # Вывод: ['h', 'l', 'l', 'w', 'r', 'l', 'd']

# Пример 6: Использование тернарного оператора в списковом включении.
numbers = [1, 2, 3, 4, 5]
result = ["четное" if x % 2 == 0 else "нечетное" for x in numbers]
# Эквивалентно:
# result = []
# for x in numbers:
#     if x % 2 == 0:
#         result.append("четное")
#     else:
#         result.append("нечетное")
print(result) # Вывод: ['нечетное', 'четное', 'нечетное', 'четное', 'нечетное']