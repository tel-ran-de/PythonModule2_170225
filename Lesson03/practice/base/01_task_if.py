number = int(input("n: "))

# Вариант-1:
# if number >= 100 and number <= 999 or number >= -999 and number <= -100:
#     print("Да")
# else:
#     print("Нет")

# Вариант-2:
if 100 <= abs(number) <= 999:
    print("Да")
else:
    print("Нет")

# [100, 999] or [-999, -100]