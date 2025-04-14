# Дана функция
def remove_duplicates(data: list):
    "Удаление дубликатов из списка"
    for item in data[:]:
        if data.count(item) > 1:
            data.remove(item)
    return data

assert remove_duplicates([1, 1, 1]) == [1]
assert remove_duplicates([]) == []
assert remove_duplicates([4]) == [4]
assert sorted(remove_duplicates([4, 5, 2, 5, 4, 2])) == [2, 4, 5]

# Протестируйте работу функции.
# Исправьте ошибки.
# Является ли функция чистой?
