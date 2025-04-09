def my_generator():
    print("Первый yield")
    yield 1
    print("Второй yield")
    yield 2
    print("Третий yield")
    yield 3


# Создаем объект-генератор
gen = my_generator()

# Итерируемся по генератору
print(next(gen))  # Выведет: Первый yield, затем 1
print(next(gen))  # Выведет: Второй yield, затем 2
print(next(gen))  # Выведет: Третий yield, затем 3

# Следующий вызов next() приведет к StopIteration
# print(next(gen))