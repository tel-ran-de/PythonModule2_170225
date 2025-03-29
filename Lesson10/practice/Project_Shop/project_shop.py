def display_menu():
    print("\nМеню:")
    print("1. Показать список товаров.")
    print("2. Добавить товар.")
    print("3. Удалить товар.")
    print("4. Обновить товар.")
    print("5. Найти товар по названию.")
    print("6. Вывести товары с ценой ниже заданной.")
    print("7. Вывести товары с количеством ниже заданного.")
    print("8. Выход. \n")


def show_items(items):
    if not items:
        print("Список товаров пуст!")
    else:
        print("Текущий список товаров: ")
        for item in items:
            print(
                f"Название: {item['name']},"
                f" Цена: {item['price']},"
                f" Количество : {item['quantity']}")


def add_item_to_inventory(items: list[dict]):
    name = input("Введите название товара: ")
    price = float(input("Введите цену товара: "))
    quantity = int(input("Введите количество товара: "))

    item = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    item = {"name": name, "price": price, "quantity": quantity}

    items.append(item)


def delete_item(items: list[dict]):
    item_to_remove = input("Введите название товара : ")
    for item in items:
        if item["name"] == item_to_remove:
            items.remove(item)
            break


def update_item(items: list[dict]):
    item_update = input("Введите товар который нужно обновить :")
    price = float(input("Введите цену товара: "))
    quantity = int(input("Введите количество товара: "))

    inventory = {"price": price, "quantity": quantity}

    for item in items:
        if item["name"] == item_update:
            item.update(inventory)
            break


def find_item_by_name(items: list[dict]):
    print("Функция поиска товара пока не реализована.")


def filter_items_by_price(items: list[dict]):
    print("Функция фильтрации по цене пока не реализована.")


def filter_items_by_quantity(items: list[dict]):
    print("Функция фильтрации по количеству пока не реализована.")


inventory = [
    {"name": "Ноутбук", "price": 1200, "quantity": 10},
    {"name": "Мышь", "price": 25, "quantity": 50},
    {"name": "Клавиатура", "price": 50, "quantity": 30},

]

while True:
    display_menu()
    choice = input("Выберите категорию: ")

    if choice == "1":
        show_items(inventory)
    elif choice == "2":
        add_item_to_inventory(inventory)
    elif choice == "3":
        delete_item(inventory)
        print("Обновленный список товаров:", inventory)
    elif choice == "4":
        update_item(inventory)
        print("Товар обновлен")
    elif choice == "5":
        find_item_by_name(inventory)
    elif choice == "6":
        filter_items_by_price(inventory)
    elif choice == "7":
        filter_items_by_quantity(inventory)
    elif choice == "8":
        confirm = input("Вы уверены, что хотите выйти? (да/нет): ").lower()
        if confirm == "да":
            print("Выход, заходите еще!")
            break
    else:
        print("Неверный выбор!")
