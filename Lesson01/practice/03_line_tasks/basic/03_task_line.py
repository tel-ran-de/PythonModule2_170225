 main
##########################


number = int(input("Введите трехзначное число: "))
first =number // 100
last = number % 10
print("Первая цифра числа =", first)
print("Последняя цифра числа =", last)

number = int(input("Введите трехзначное число: ")) # 123
first = number // 100
last = number % 10
print(f"Первая цифра числа = {first}")
print(f"Последняя цифра числа = {last}")

# 123 -> 3
# 123 % 10 -> 3
# 458 % 10 -> 8

# 123 -> 1
# 123 // 100 -> 1
# 785 // 100 -> 7

# 123 -> 2
# 123 // 10 -> 12 % 10 -> 2
 main
