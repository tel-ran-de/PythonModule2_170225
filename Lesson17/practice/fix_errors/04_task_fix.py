# Дана функция
def count_vowels(text: str) -> int:
    "Подсчет гласных "
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count


def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("apple") == 2
    assert count_vowels("orange") == 3


# Протестируйте работу функции.
# Исправьте ошибки.
# Является ли функция чистой?
test_count_vowels()
