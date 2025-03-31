from pprint import pprint
# "Добавление нового товара"
#
# Создайте список словарей, представляющих несколько товаров.
# Напишите функцию для добавления нового товара.
# Функция должна запрашивать у пользователя название товара, цену и количество.
# Функция должна создавать словарь товара с введенными данными и добавлять его в конец списка.
# Вызовите функцию для добавления нового товара и выведите обновленный список на экран.

def add_item_to_inventory(items: list[dict]) -> None:
    """Добавляет товар в инвентарь"""
    name = input("Введите название товара: ")
    price = float(input("Введите цену товара: "))
    quantity = int(input("Введите количество товара: "))
    item = {"name": name,"price": price,"quantity": quantity}
    items.append(item)


inventory = [
    {"name": "Ноутбук", "price": 1200, "quantity": 10},
    {"name": "Мышь", "price": 25, "quantity": 50},
    {"name": "Клавиатура", "price": 50, "quantity": 30},
]

add_item_to_inventory(inventory)
pprint(inventory)
