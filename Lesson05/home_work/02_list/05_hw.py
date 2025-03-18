# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Выхухоль", "Василий", "Петр"]
len_name = 0
i_names = 0
for i, name in enumerate(names):
    # print(f"{i} {name} {len(name)}")
    if len_name < len(name): # <= последнее max
        len_name = len(name)
        i_names = i
print(names[i_names])

# ChatGPT Das is BimBa!!!   ;-)
print(f"\n{max(names, key=len)}")
