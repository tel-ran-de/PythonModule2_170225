# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу не используя строки

# def palindrome(number):
    # return number == int(str(number)[::-1])
    # return str(number) == str(number)[::-1]

def palindrome(number):
    reverse_number = 0
    copy_number = number
    while copy_number > 0:
        digit = copy_number % 10
        reverse_number = reverse_number * 10 + digit
        copy_number = copy_number // 10

    return reverse_number == number


# Тестируем функцию
# palindrome(6543)

# 3 | 4 -> 34 -> 3*10 + 4 -> 34*10 + 5 -> 345
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))
print(palindrome(1))

# Подсказка:
# Самый простой способ решить задачу, работать с полученным числом как со строкой
# Преобразование к строке:  str(1234) --> "1234"
# Переворот строки:         "1234"[::-1] --> "4321"


# 12345 -> 54321

# 12345 -> 1 2 3 4 5 -> 54321

# 12345 % 10 -> 5
# 12345 // 10 -> 1234
# 1234 % 10 -> 4
# 1234 // 10 -> 123
#
# 5 4 3 2 1 -> 54321