# Напишите декоратор timer, который измеряет время выполнения декорируемой функции и выводит его в консоль.


import time


def timer(original_function):
    def wrapper_function(*args, **kwargs):
        # Код до вызова оригинальной функции
        start_time = time.time()
        result = original_function(*args, **kwargs)
        end_time = time.time()
        delta_time = end_time - start_time
        print(f"Фунция работала {delta_time}")
        # Код после вызова оригинальной функции
        return result
    return wrapper_function


@timer
def my_function():
    time.sleep(1)
    print("Функция выполнена")


my_function()
my_function()
my_function()
my_function()
my_function()
