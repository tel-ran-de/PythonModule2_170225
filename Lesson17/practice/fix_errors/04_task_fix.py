# Дана функция
def count_vowels(text: str) -> int:
    "Подсчет гласных "
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

# Протестируйте работу функции.
# Исправьте ошибки.
# Является ли функция чистой?
