def is_even(num):
    return num % 2 == 0


n = int(input("Введите число: "))
if is_even(n):
    print("Число четное")
else:
    print("Число не четное")
