# Даны функции
def average(numbers: list) -> float:
    "Нахождение среднеарифметического"
    if not numbers:
        return 0
    total = sum(numbers)
    return total / len(numbers)


def get_unique_elements(data: list) -> list:
    unique = []
    for item in data:
        if item not in unique:
            unique.append(item)

    return unique


if __name__ == "__main__":
    assert average([]) == 0
    assert average([0]) == 0
    assert average([10, -10, 0]) == 0
    assert average([1, 2, 3]) == 2.0
    assert average([12, 20, 8, 10]) == 12.5
    assert round(average([2.5, -5.5, 10, 0, -6.5, 3.5]), 2) == 0.67
    assert round(average([12, 20, 8, 8, -4, 6]), 2) == 8.33

    assert get_unique_elements([3, 4, 5]) == [3, 4, 5]
    assert get_unique_elements([3, 4, 5, 4, 5]) == [3, 4, 5]
    assert get_unique_elements([]) == []
    assert get_unique_elements([2, 2, 2, 2, 2, 2]) == [2]
    assert get_unique_elements([10, 7, 6, 7, 8]) == [10, 7, 6, 8]
    assert get_unique_elements([1 / 2]) == [0.5]
    assert get_unique_elements([1, "1", 1]) == [1, "1"]
    assert get_unique_elements(["hello", "hello", "by"]) == ["hello", "by"]
# Протестируйте работу функции.
# Исправьте ошибки.
# Является ли функция чистой?
