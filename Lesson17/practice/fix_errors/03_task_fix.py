# Дана функция
def remove_duplicates(data: list):
    "Удаление дубликатов из списка"
    for item in data[:]:
        if data.count(item) > 1:
            data.remove(item)
    return data

<<<<<<< HEAD

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 1, 2, 3]) == [1, 2, 3]
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

=======
assert remove_duplicates([1, 1, 1]) == [1]
assert remove_duplicates([]) == []
assert remove_duplicates([4]) == [4]
assert sorted(remove_duplicates([4, 5, 2, 5, 4, 2])) == [2, 4, 5]
>>>>>>> 68b338dc43d0d6145b3c52e09c1e88e0928f2085

# Протестируйте работу функции.
# Исправьте ошибки.
# Является ли функция чистой?
test_remove_duplicates()
