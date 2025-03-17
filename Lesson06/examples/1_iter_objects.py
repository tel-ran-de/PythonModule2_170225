# Итерируемые объекты — объекты, которые позволяют последовательно перебирать элементы коллекции.
# В Python это: списки, кортежи, строки и другие типы данных.

numbers = [1, 2, 3]
iterator = iter(numbers)  # Получение итератора

number = next(iterator) # Получение следующего элемента
print(number)
number = next(iterator) # Получение следующего элемента
print(number)
number = next(iterator) # Получение следующего элемента
print(number)

# Если вызвать еще раз, то будет выброшено исключение StopIteration
# Раскомментируйте код ниже, чтобы убедиться:
# number = next(iterator) # Получение следующего элемента
# print(number)

# Цикл for in так и работает:
# 1. получает iterator из итерируемого объекта
for number in numbers: # 2. Вызывает next(), для получения элементов и ожидает StopIteration
    print(number)