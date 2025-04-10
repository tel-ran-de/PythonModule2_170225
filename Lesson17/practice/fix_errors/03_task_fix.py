# Дана функция
def remove_duplicates(data: list):
    "Удаление дубликатов из списка"
    for item in data:
        if data.count(item) > 1:
            data.remove(item)
    return data


def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 1, 2, 3]) == [1, 2, 3]
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


# Протестируйте работу функции.
# Исправьте ошибки.
# Является ли функция чистой?
test_remove_duplicates()
