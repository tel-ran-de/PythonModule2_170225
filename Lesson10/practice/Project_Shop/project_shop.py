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


display_menu()


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

    for item in items:
        if item["name"] == item_update:
            print(f"Товар найден : {item}")

            print("Что вы хотите обновить?")
            print("1 - Цена")
            print("2 - Количество")
            print("3 - И цену, и количество")
            choice = input("Введите номер действия (1, 2 или 3): ")

            # Проверка выбора
            if choice not in {"1", "2", "3"}:
                print("Ошибка: Неверный выбор.")
                return

            # Обновляем только цену
            if choice in {"1", "3"}:
                price_input = input("Введите новую цену товара: ")
                if price_input.replace(".", "", 1).isdigit():  # Проверяем, что цена — число
                    new_price = float(price_input)
                    if new_price < 0:
                        print("Ошибка: Цена не может быть отрицательной.")
                        return
                    item["price"] = new_price
                else:
                    print("Ошибка: Цена должна быть числом.")
                    return

            # Обновляем только количество
            if choice in {"2", "3"}:
                quantity_input = input("Введите новое количество товара: ")
                if quantity_input.isdigit():  # Проверяем, что количество — положительное целое число
                    new_quantity = int(quantity_input)
                    if new_quantity < 0:
                        print("Ошибка: Количество не может быть отрицательным.")
                        return
                    item["quantity"] = new_quantity
                else:
                    print("Ошибка: Количество должно быть целым числом.")
                    return

            # Сообщение об успешном обновлении
            print(f"Товар обновлен: {item}")
            return

    print(f"Ошибка: Товар '{item_update}' не найден.")


def find_item_by_name(items: list[dict]):
    find_item = input("Введите поисковое слово :").lower()
    matching_items = [item for item in items if 'name' in item and find_item in item['name'].lower()]

    if matching_items:
        print("Найденные товары:")
        for match in matching_items:
            print(match)
    else:
        print("Соответствующих товаров не найдено.")


def filter_items_by_price(items: list[dict]):
    filter_price_min = float(input("Введите  искомую цену : "))
    matching_price = [item for item in items if 'price' in item and item['price'] <= filter_price_min]
    if matching_price:
        print("Найденные цены : ")
        for match in matching_price:
            print(match)
    else:
        print("Такой цены не существует.")


def filter_items_by_quantity(items: list[dict]):
    find_quantity = int(input("Введите искомое количество товара : "))
    matching_quantity = [item for item in items if 'quantity' in item and item['quantity'] <= find_quantity]
    if matching_quantity:
        print("Найденное по количеству товара : ")
        for match in matching_quantity:
            print(match)
    else:
        print("Такого количества товара не существует .")


inventory = [
    {"name": "Ноутбук", "price": 1200, "quantity": 10},
    {"name": "Мышь", "price": 25, "quantity": 50},
    {"name": "Клавиатура", "price": 50, "quantity": 30},

]

while True:

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
        print("Товар найден")
    elif choice == "6":
        filter_items_by_price(inventory)
        print("Цены ниже указанной суммы :")
    elif choice == "7":
        filter_items_by_quantity(inventory)
        print("Количество ниже указанного :")
    elif choice == "8":
        confirm = input("Вы уверены, что хотите выйти? (y/n): ").lower()
        if confirm == "y" or confirm == "yes":
            print("Выход, заходите еще!")
            break
    else:
        print("Неверный выбор!")
