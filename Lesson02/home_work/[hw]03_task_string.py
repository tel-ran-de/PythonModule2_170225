# Посчитайте количество согласных(латинских) букв в данной строке.

import re

def count_consonants(text):
    return len(re.findall(r'[bcdfghjklmnpqrstvwxyz]', text, re.I))

text = "Hello, World!"
print(count_consonants(text))
