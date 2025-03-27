# Напишите декоратор to_string, который преобразует результат выполнения декорируемой функции в строку.


def to_string(original_function):
    def wrapper_function(*args, **kwargs):
        # Код до вызова оригинальной функции
        result = original_function(*args, **kwargs)
        # Код после вызова оригинальной функции
        return str(result)

    return wrapper_function

@to_string
def calculate_sum(a, b):
    return a + b

print(type(calculate_sum(5, 10)))
