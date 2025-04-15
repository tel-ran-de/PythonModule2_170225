# "Поиск товара в списке словарей"
#
# Создайте список словарей, представляющих несколько товаров (минимум 4 товара).
# Напишите функцию, которая принимает название товара и список словарей в качестве аргументов.
# Функция должна возвращать словарь товара с указанным названием или None, если товар не найден.
# Вызовите функцию для поиска товара и выведите результат.

def find_item_by_name(items: list[dict], name: str) -> dict | None:
    for item in items:
        if item[name] == name:
            return item


items = [
    {"name": "шапки", "cost": 12.5, "count": 10},
    {"name": "кеды", "cost": 6.5, "count": 10},
    {"name": "носки", "cost": 0.5, "count": 50},
    {"name": "трусы", "cost": 5.5, "count": 10}
]

for item in items:
    if item["name"] == name:
        return item

items = [
    {"name": "Кеды", "cost": 12.5, "count": 10},
    {"name": "Кепка", "cost": 6.2, "count": 12},
    {"name": "Носки", "cost": 0.5, "count": 50},
    {"name": "Рубашка", "cost": 5.45, "count": 17},
]

result_item = find_item_by_name(items, "Тапки")
print(result_item)
