# Задача: Подсчитать количество гласных(русских) букв во введенной строке без учета регистра.
# Решение:

# text = "мАма мЫла раму"
# vowels = "ауоыэяюёие"
#
# num_vowels = 0
# for char in text.lower():
#     if char in vowels:
#         num_vowels += 1
#
# print(num_vowels)


# Оформите решение задачи в виде функции

def count_vowels(text):
    vowels = "ауоыэяюёие"
    num_vowels = 0
    for char in text.lower():
        if char in vowels:
            num_vowels += 1
    return num_vowels

print(count_vowels("прИвет мир!"))

# 1. Убираем дубликаты(сокращаем код)
# 2. Упрощает тестирование (модульный код)
# 3. Повторное использование кода
# 4. Разделение обязанностей