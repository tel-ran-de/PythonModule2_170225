# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
# Найдите:
print("Товары на складе представлены брэндами: ")

for el in items:
    print(el["brand"])
# TODO: your code here

print("На складе больше всего товаров брэнда(ов): ")

# TODO: your code here
for el in items:
    if el["brand"] == max(el["brand"] for el in items):
        print((el["brand"]))


print("На складе самый дорогой товар брэнда(ов): ")
for el in items:
    if el["price"] == max(el["price"] for el in items):
        print((el["brand"]))
# TODO: your code here
