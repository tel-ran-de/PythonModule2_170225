# Напишите декоратор cache, который кэширует результаты выполнения декорируемой функции.
# Если функция вызывается с теми же аргументами, что и ранее,
# декоратор должен возвращать сохраненный результат, не выполняя функцию заново.

import time

def cache(func):
    # Ваш код здесь
    pass

@cache
def expensive_calculation(n):
    time.sleep(1)
    return n * n

print(expensive_calculation(5))
print(expensive_calculation(5))