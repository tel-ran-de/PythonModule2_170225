my_list = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Исходный список: {my_list}")

# Сортировка списка с помощью sorted()
sorted_list = sorted(my_list)
print(f"Отсортированный список (sorted()): {sorted_list}")
print(f"Исходный список после sorted(): {my_list}") # Исходный список не изменился

# Сортировка кортежа
my_tuple = (3, 1, 4)
sorted_tuple = sorted(my_tuple)
print(f"Отсортированный кортеж (sorted()): {sorted_tuple}") # Возвращает список

# Сортировка строки
my_string = "hello"
sorted_string = sorted(my_string)
print(f"Отсортированная строка (sorted()): {sorted_string}") # Возвращает список символов

# Сортировка по убыванию с помощью sorted()
reversed_list = sorted(my_list, reverse=True)
print(f"Сортировка по убыванию (sorted()): {reversed_list}")

# Сортировка списка словарей по значению ключа
data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
sorted_data = sorted(data, key=lambda item: item['age'])
print(f"Сортировка словарей по возрасту (sorted()): {sorted_data}")