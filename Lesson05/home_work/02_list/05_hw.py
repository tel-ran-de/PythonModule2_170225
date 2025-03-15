# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них




names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
long_name = ""

i = 0
for name in names :
    if len(name) > len(long_name) :
       long_name = name

print(long_name)
