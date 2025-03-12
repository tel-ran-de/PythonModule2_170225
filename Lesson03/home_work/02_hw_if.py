a = int(input("Количество коров"))
if a % 100 == 1 and a != 11 :
    print("Корова")
elif a % 100 == 2 or a % 100 == 3 or a % 100 == 4 and a % 100 != 12 and a % 100 != 13 and a % 100 != 14 :
    print("Коровы")
else:
    print("Коров")