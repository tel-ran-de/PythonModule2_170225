a = int(input("Количество коров"))
if a % 10 == 1 and a != 11 :
    print("Корова")
elif a % 10 == 2 or a % 10 == 3 or a % 10 == 4  :
    print("Коровы")
else:
    print("Коров")