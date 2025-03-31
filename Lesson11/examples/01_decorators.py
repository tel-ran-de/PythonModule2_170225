# Простой декоратор
def my_decorator(func):
    def wrapper():
        print("Что-то происходит перед функцией.")
        func()
        print("Что-то происходит после функции.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Вывод:
# Что-то происходит перед функцией.
# Hello!
# Что-то происходит после функции.


# Декоратор логирование вызовов функций
def log(func):
    def wrapper(*args, **kwargs):
        print(f'Вызвана функция {func.__name__} с аргументами {args}, {kwargs}')
        return func(*args, **kwargs)
    return wrapper

@log
def multiply(x, y):
    return x * y

multiply(3, 4)
# Вывод:
# Вызвана функция multiply с аргументами (3, 4), {}


# Декоратор с параметрами
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Привет!")

say_hello()
# Вывод:
# Привет!
# Привет!
# Привет!