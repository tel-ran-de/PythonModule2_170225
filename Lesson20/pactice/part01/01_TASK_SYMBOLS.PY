## "Квадрат символами"


while True:
    n = int(input("Сторона квадрата : "))

    if 2 <= n <= 20:
        print("*" * n)

        for i in range(n - 2):
            print("*" + ' ' * (n - 2) + "*")
        print("*" * n)

           
    else:
        print("число должно быть положительным от 3 до 19 !")
        break
