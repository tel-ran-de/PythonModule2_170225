# Напишите декоратор to_string, который преобразует результат выполнения декорируемой функции в строку.


def to_string(func):
    # Ваш код здесь
    pass

@to_string
def calculate_sum(a, b):
    return a + b

print(calculate_sum(5, 10))
