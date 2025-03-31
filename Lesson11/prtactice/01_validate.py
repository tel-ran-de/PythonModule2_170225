# Напишите декоратор validate_arguments, который проверяет,
# что все аргументы декорируемой функции являются положительными числами.
# Если какой-либо аргумент не удовлетворяет этому условию, декоратор должен выводить сообщение об ошибке.


def validate_arguments(original_function):
    def wrapper_function(*args, **kwargs):
        # Код до вызова оригинальной функции
        for arg in args:
            if arg < 0:
                print(f"аргумент {arg} отрицательный")
                return None
        result = original_function(*args, **kwargs)
        # Код после вызова оригинальной функции
        return result

    return wrapper_function


@validate_arguments
def calculate_sum(a, b):
    return a + b


print(calculate_sum(5, 10))
print(calculate_sum(-1, 5))
