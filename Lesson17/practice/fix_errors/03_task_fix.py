# Дана функция
def remove_duplicates(data: list):
    "Удаление дубликатов из списка"
    for item in data:
        if data.count(item) > 1:
            data.remove(item)
    return data

# Протестируйте работу функции.
# Исправьте ошибки.
# Является ли функция чистой?
