## "Квадрат символами"


n = int(input("Введите число от 2 до 19 :"))

if 2 <= n <= 20:
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end="")

            else:
                print(" ", end="")
        print()

else:
    print("Введите число в диапазоне от 2 до 19 ! ")
