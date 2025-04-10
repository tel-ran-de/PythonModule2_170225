# apply_operation является функцией высшего порядка, так как она принимает другие функции (square и cube) в качестве аргументов

def apply_operation(func, x):
    """Применяет функцию func к значению x."""
    return func(x)


def square(n):
    """Возвращает квадрат числа n."""
    return n * n


def cube(n):
    """Возвращает куб числа n."""
    return n * n * n


# Используем apply_operation с различными функциями
result_square = apply_operation(square, 5)
print(f"Квадрат 5: {result_square}")  # Вывод: Квадрат 5: 25

result_cube = apply_operation(cube, 5)
print(f"Куб 5: {result_cube}")  # Вывод: Куб 5: 125
