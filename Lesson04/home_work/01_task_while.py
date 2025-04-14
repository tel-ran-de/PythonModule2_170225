cost = float(input("price:"))  # Цена
m = int(input("pices:"))  # Количество товара
if m < 0:  # Цикл 1
    print("Количество товара не может быть отрицательным !")
n = 1
while n < m + 1:  # Цикл 2
    print(f" Цена за {n} шт :{cost * n} еек")

    n += 1
