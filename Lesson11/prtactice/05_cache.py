# Напишите декоратор cache, который кэширует результаты выполнения декорируемой функции.
# Если функция вызывается с теми же аргументами, что и ранее,
# декоратор должен возвращать сохраненный результат, не выполняя функцию заново.

import time

def cache(original_function):
    cached_results = {}
    def wrapper_function(*args, **kwargs):
        # Код до вызова оригинальной функции
        # print(f"{cached_results=}")
        key = (args, tuple(kwargs.items()))
        if key in cached_results.keys(): # значение уже вычислялось
            print("Берем результат из кэша")
            return cached_results[key]
        else: # значение еще НЕ вычислялось
            print("Вычисляем новый рельтат и сохраняем в кэш")
            result = original_function(*args,  **kwargs)
            cached_results[key] = result
            return result
    return wrapper_function

@cache
def expensive_calculation(n):
    time.sleep(1)
    return n * n

@cache
def average(*args):
    return sum(args)/ len(args)

@cache
def greed(name):
    return f"Hello, {name}"

# print(expensive_calculation(5))
# print(expensive_calculation(5))
# print(average(4, 6, 2, 0, -4, 3))
# print(average(4, 6, 2, 0, -4, 3))
# print(average(4, 6, 2, 0, -4, 3))
print(greed(name="Alex"))
print(greed(name="Alex"))
print(greed(name="Petr"))
print(greed(name="Petr"))


