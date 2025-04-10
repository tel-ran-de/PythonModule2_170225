# Пример-1: чистая функция
def add(x, y):
    """Чистая функция: всегда возвращает x + y для одних и тех же x и y."""
    return x + y


result1 = add(5, 3)  # result1 всегда будет 8
result2 = add(5, 3)  # result2 также всегда будет 8

# Пример-2: Нечистая функция
counter = 0


def increment_and_add(x):
    """Нечистая функция: результат зависит от глобальной переменной counter."""
    global counter
    counter += 1
    return x + counter


print(increment_and_add(5))  # Может вывести 6 (если counter был 0)
print(increment_and_add(5))  # Может вывести 7 (если counter стал 1)


# Пример-3: чистая функция
def multiply(x, y):
    """Чистая функция: просто возвращает произведение, ничего не меняя."""
    return x * y


a = 5
b = 10
result = multiply(a, b)
print(f"Результат: {result}")  # Выводит 50
print(f"a: {a}, b: {b}")  # a и b остаются неизменными (5 и 10)


# Пример-4: Нечистая функция
def append_to_list(data, item):
    """Нечистая функция: изменяет переданный список data."""
    data.append(item)
    return data


my_list = [1, 2]
new_list = append_to_list(my_list, 3)
print(f"new_list: {new_list}")  # Выводит [1, 2, 3]
print(f"my_list: {my_list}")  # my_list также изменился и стал [1, 2, 3]
