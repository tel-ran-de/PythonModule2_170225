# Проверка, является ли заданный год началом нового тысячелетия
#
# Напишите, которая принимает целое число, представляющее год,
# и возвращает True, если этот год является началом нового тысячелетия (например, 2001),
# и False в противном случае.

def is_millennium_start(year: int) -> bool:
    str_year = str(year)
    if str_year[-3:] == "001" or str_year == "1":
        return True
    return False

def is_millennium_start1(year: int) -> bool:
    if year == 1 or (year - 1) % 1000 == 0:
        return True
    return False

# Пример использования
assert is_millennium_start(1) == True         # первый год — начало первого тысячелетия
assert is_millennium_start(1000) == False     # это конец 1-го тысячелетия
assert is_millennium_start(1001) == True      # начало второго тысячелетия
assert is_millennium_start(2001) == True      # начало третьего тысячелетия
assert is_millennium_start(2100) == False     # не начало тысячелетия
assert is_millennium_start(3001) == True      # начало четвертого тысячелетия
assert is_millennium_start(11) == False       # не подходит
assert is_millennium_start(999) == False      # не подходит

assert is_millennium_start1(1) == True         # первый год — начало первого тысячелетия
assert is_millennium_start1(1000) == False     # это конец 1-го тысячелетия
assert is_millennium_start1(1001) == True      # начало второго тысячелетия
assert is_millennium_start1(2001) == True      # начало третьего тысячелетия
assert is_millennium_start1(2100) == False     # не начало тысячелетия
assert is_millennium_start1(3001) == True      # начало четвертого тысячелетия
assert is_millennium_start1(11) == False       # не подходит
assert is_millennium_start1(999) == False      # не подходит

# Пример использования
year1 = 2001
year2 = 2100
print(f"{year1} - начало тысячелетия: {is_millennium_start(year1)}")
print(f"{year2} - начало тысячелетия: {is_millennium_start(year2)}")
