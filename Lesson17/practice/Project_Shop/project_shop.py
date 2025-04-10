def add_item(inventory):
    """Добавляет новый товар в инвентарь."""
    name = input("Введите название товара: ").strip()
    for item in inventory:
        if item['name'] == name:
            print("Ошибка: Товар с таким названием уже существует.")
            return
    while True:
        try:
            price = float(input("Введите цену товара: "))
            if price <= 0:
                print("Ошибка: Цена должна быть положительным числом.")
            else:
                break
        except ValueError:
            print("Ошибка: Введите корректное число для цены.")

    # TODO-1: добавьте обработку ввода некорректного количества товаров (по аналогии с ценой)
    quantity = int(input("Введите количество товара: "))

    inventory.append({"name": name, "price": price, "quantity": quantity})
    print(f"Товар '{name}' успешно добавлен.")


def remove_item(inventory):
    """Удаляет товар из инвентаря по названию."""
    name = input("Введите название товара для удаления: ").strip()
    for i, item in enumerate(inventory):
        if item['name'] == name:
            del inventory[i]
            print(f"Товар '{name}' успешно удален.")
            return
    print(f"Товар с названием '{name}' не найден.")


def update_item(inventory):
    """Обновляет информацию о товаре."""
    name = input("Введите название товара для обновления: ").strip()
    for item in inventory:
        if item['name'] == name:
            print("Какое поле вы хотите обновить?")
            print("1. Цена")
            print("2. Количество")
            choice = input("Введите номер опции: ")
            if choice == '1':
                while True:
                    try:
                        price = float(input("Введите новую цену: "))
                        if price <= 0:
                            print("Ошибка: Цена должна быть положительным числом.")
                        else:
                            item['price'] = price
                            print(f"Цена товара '{name}' успешно обновлена.")
                            break
                    except ValueError:
                        print("Ошибка: Введите корректное число для цены.")
            elif choice == '2':
                # TODO-2: добавьте обработку ввода некорректного нового количества товаров (по аналогии с ценой)
                quantity = int(input("Введите новое количество: "))
                item['quantity'] = quantity
                print(f"Количество товара '{name}' успешно обновлено.")

    print(f"Товар с названием '{name}' не найден.")


def search_item(inventory):
    """Поиск товара по части названия."""
    query = input("Введите часть названия товара для поиска: ").strip().lower()
    found_items = [item for item in inventory if query in item['name'].lower()]
    if found_items:
        print("Найденные товары:")
        for item in found_items:
            print(f"Название: {item['name']}, Цена: {item['price']}, Количество: {item['quantity']}")
    else:
        print("Товары не найдены.")


def display_inventory(inventory):
    """Выводит список всех товаров."""
    # TODO-3: если в списке нет товаров, выведите "Инвентарь пуст"
    print("Список товаров:")
    for i, item in enumerate(inventory):
        print(f"{i + 1}. Название: {item['name']}, Цена: {item['price']}, Количество: {item['quantity']}")


def display_below_price(inventory):
    """Выводит товары с ценой ниже заданной."""
    while True:
        try:
            price_limit = float(input("Введите максимальную цену: "))
            if price_limit < 0:
                print("Ошибка: Цена не может быть отрицательной.")
            else:
                break
        except ValueError:
            print("Ошибка: Введите корректное число для цены.")
    below_price_items = [item for item in inventory if item['price'] < price_limit]
    # TODO-4: если товары ниже указанной цены не найдены, выведите "Нет товаров с ценой ниже"
    print(f"Товары с ценой ниже {price_limit}:")
    for item in below_price_items:
        print(f"Название: {item['name']}, Цена: {item['price']}, Количество: {item['quantity']}")


def display_below_quantity(inventory):
    """Выводит товары с количеством ниже заданного."""
    while True:
        try:
            quantity_limit = int(input("Введите максимальное количество: "))
            if quantity_limit < 0:
                print("Ошибка: Количество не может быть отрицательным.")
            else:
                break
        except ValueError:
            print("Ошибка: Введите целое число для количества.")
    below_quantity_items = [item for item in inventory if item['quantity'] < quantity_limit]
    # TODO-5: если товары с количеством ниже не найдены, выведите "Нет товаров с количеством ниже"
    print(f"Товары с количеством ниже {quantity_limit}:")
    for item in below_quantity_items:
        print(f"Название: {item['name']}, Цена: {item['price']}, Количество: {item['quantity']}")


def main():
    """Основная функция приложения."""
    inventory = []
    while True:
        print("\nМеню:")
        print("1. Показать список товаров.")
        print("2. Добавить товар.")
        print("3. Удалить товар.")
        print("4. Обновить товар.")
        print("5. Найти товар по названию.")
        print("6. Вывести товары с ценой ниже заданной.")
        print("7. Вывести товары с количеством ниже заданного.")
        print("8. Выход.")

        choice = input("Выберите операцию: ")
        # TODO-0: реализуйте выбор пунктов меню, используя словарь menu_options = {}
        if choice == '1':
            display_inventory(inventory)
        elif choice == '2':
            add_item(inventory)
        elif choice == '3':
            remove_item(inventory)
        elif choice == '4':
            update_item(inventory)
        elif choice == '5':
            search_item(inventory)
        elif choice == '6':
            display_below_price(inventory)
        elif choice == '7':
            display_below_quantity(inventory)
        elif choice == '8':
            print("Завершение работы программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите операцию из меню.")


if __name__ == "__main__":
    main()
