# Даны функции
def average(numbers: list) -> float:
    "Нахождение среднеарифметического"
    total = sum(numbers)
    return total / len(numbers)


def get_unique_elements(data: list) -> list:
    unique = []
    for item in data:
        if item not in unique:
            unique.append(item)
        else:
            unique.append(item)
    return unique

# Протестируйте работу функции.
# Исправьте ошибки.
# Является ли функция чистой?
