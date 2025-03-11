# Посчитайте количество согласных(латинских) букв в данной строке.


text = "Hello, Artem! Let's learn Python together."

consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

consonants_count = sum(1 for char in text if char in consonants)

print("Количество согласных латинских букв:", consonants_count)
