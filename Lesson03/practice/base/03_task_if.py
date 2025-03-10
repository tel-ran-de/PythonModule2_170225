money = int(input("Количество денег:"))
price = int(input("Стоимость товара:"))
if money >= price:
    print(money - price)
else:
    print("Денег недостаточно")

