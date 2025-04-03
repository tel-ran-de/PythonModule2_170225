def display_menu():
    """Отображает меню."""
    print("\nМеню:")
    print("1. Показать список товаров.")
    print("2. Добавить товар.")
    print("3. Удалить товар.")
    print("4. Обновить товар.")
    print("5. Найти товар по названию.")
    print("6. Вывести товары с ценой ниже заданной.")
    print("7. Вывести товары с количеством ниже заданного.")
    print("8. Выход. \n")


def show_items(items: list[dict]): # 1
    print("show_items")

def find_item_by_name(items: list[dict], item_name): # 5
    print("find_item_by_name")

def filter_items_lower_price(items: list[dict]): # 6
    price = int(input("Укажите минимальную цену: "))

    for item in items:
        if item["price"] < price:
            print(f"{item['name']} Цена: {item['price']} Количество: {item['quantity']}")


inventory = [
    {"name": "Ноутбук", "price": 1200, "quantity": 10},
    {"name": "Мышь", "price": 25, "quantity": 50},
    {"name": "Клавиатура", "price": 50, "quantity": 30},
]
# Menu
while True:
    display_menu()
    choice = input("Выберите действие: ")

    if choice == "1":
        show_items(inventory)
    elif choice == "5":
        find_item_by_name(inventory, ...)
    elif choice == "6":
        filter_items_lower_price(inventory)
    elif choice == "8":
        break
