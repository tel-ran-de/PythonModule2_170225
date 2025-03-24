# Дан словарь и ключ.
# Напишите программу, которая возвращает значение по ключу.
# Если ключ отсутствует, возвращает "Ключ не найден".

my_dict = {"a": 0, "b": 2, "c": 3}
key = input("Enter key: ")

# if key in my_dict:
#     value = my_dict[key]
#     print(f" {value}")
# else:
#     print("Ключ не найден")

if my_dict.get(key) is not None:
    print(my_dict[key])
else:
    print("Ключ не найден")
