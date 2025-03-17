# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

name_count = len(names)
n = 1
for name in names:
    if n >= name_count:
        print(f"{name}")
        break
    print(f"{name}, ",end="")
    n += 1
print("*********Вариант 2******")
print(", ".join(names))

# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр
