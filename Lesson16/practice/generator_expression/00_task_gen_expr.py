# "ASCII коды символов строки"
# Генераторное выражение, возвращающее ASCII коды каждого символа в заданной строке.

string = "hello world"

gen = (ord(char) for char in string)

print(list(gen))