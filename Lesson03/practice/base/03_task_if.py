cash = int(input("руб"))
price = int(input("цена"))
sum = cash - price

if cash >= price :
    print(sum)
else:
    print("Денег недостаточно")