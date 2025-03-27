# Напишите декоратор timer, который измеряет время выполнения декорируемой функции и выводит его в консоль.


import time


def timer(func):
    # Ваш код здесь
    pass


@timer
def my_function():
    time.sleep(2)
    print("Функция выполнена")


my_function()
