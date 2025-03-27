# Напишите декоратор validate_arguments, который проверяет,
# что все аргументы декорируемой функции являются положительными числами.
# Если какой-либо аргумент не удовлетворяет этому условию, декоратор должен выводить сообщение об ошибке.


def validate_arguments(func):
    def wrapper(a, b):
        if a >= 0 and b >= 0:
            return func(a, b)
        else:

            print("Error: negative arguments")
            return None

    return wrapper


@validate_arguments
def calculate_sum(a, b):
    return a + b


print(calculate_sum(5, 10))
print(calculate_sum(-1, 5))
