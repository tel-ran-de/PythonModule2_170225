# Задача: Подсчитать количество гласных(русских) букв во введенной строке без учета регистра.
# Решение:

text = "мАма мЫла раму"
vowels = "ауоыэяюёие"

num_vowels = 0
for char in text.lower():
    if char in vowels:
        num_vowels += 1

print(num_vowels)


# Оформите решение задачи в виде функции

def count_vowels():
    pass
