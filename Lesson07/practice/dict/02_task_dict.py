# Дана строка.
# Напишите программу, которая подсчитывает частоту каждого символа в строке.

text = "hello world hello python world"

num_chars = {}
for char in text:
    if char in num_chars:
        num_chars[char] += 1
    else:
        num_chars[char] = 1

print(num_chars)