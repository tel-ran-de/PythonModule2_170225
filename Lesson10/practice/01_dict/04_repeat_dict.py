# "Работа со списком товаров"
#
# Создайте список словарей, представляющих несколько товаров (минимум 4 товара).
# Выведите на экран нумерованный список всех названий товаров

<<<<<<< HEAD
items =[
    {"name" : "шапки",    "cost" : 12.5,   "count" : 10},
    {"name" : "кеды",    "cost" : 6.5,   "count" : 10},
    {"name" :  "носки",  "cost" :  0.5,   "count" : 50},
    {"name" : "трусы",   "cost" : 5.5,   "count" : 10}
    ]

i = 1
for item in items:
    print(item["name"])
    i+=1
=======
items = [
    {"name": "Кеды", "cost": 12.5, "count": 10},
    {"name": "Кепка", "cost": 6.2, "count": 12},
    {"name": "Носки", "cost": 0.5, "count": 50},
    {"name": "Рубашка", "cost": 5.45, "count": 17},
]


for i, item in enumerate(items, 1):
    print(i, item["name"])
>>>>>>> 79e048c3d328c1b37987ef1362fc72e94e4190b3

