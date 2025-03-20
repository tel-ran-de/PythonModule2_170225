# Дана строка.
# Напишите программу, которая подсчитывает частоту каждого символа в строке.

text = "hello world hello python world"
<<<<<<< HEAD
textlist = list(text)
print(textlist)
# TODO: your code here
=======

num_chars = {}
for char in text:
    if char in num_chars:
        num_chars[char] += 1
    else:
        num_chars[char] = 1

print(num_chars)
>>>>>>> 154385c3b5f72787a35f27bb8b6927527704f159
