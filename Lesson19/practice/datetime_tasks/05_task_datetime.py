# Напишите функцию is_leap_year(year), которая принимает целое число, представляющее год,
# и возвращает True, если год является високосным, и False в противном случае.
# (Напоминание: високосный год делится на 4, кроме годов, делящихся на 100, но не на 400).

def is_leap_year(year: int) -> bool:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


# Любой год, который делится на 4 без остатка, является високосным годом


# Допишите код здесь


# Пример использования
year1 = 2022
year2 = 2100
print(f"{year1} - високосный год: {is_leap_year(year1)}")
print(f"{year2} - високосный год: {is_leap_year(year2)}")

# TODO: напишите тесты для функции, используя оператор assert
assert is_leap_year(2000) == True
assert is_leap_year(1900) == False
assert is_leap_year(2000) == True

print("все проверки прошли успешно")
