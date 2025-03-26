def reverse_string(s):
    """
    Переворачивает строку.
    """

    # Базовый случай: пустая строка или строка из одного символа
    if len(s) <= 1:
        return s
    # Рекурсивный случай: последний символ + перевернутая оставшаяся часть строки
    else:
        return s[-1] + reverse_string(s[:-1])

# Пример использования
my_string = "hello"
print(reverse_string(my_string))  # Вывод: olleh