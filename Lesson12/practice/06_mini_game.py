# Задача "Игра "Камень, ножницы, бумага"

# Создайте функцию, которая имитирует игру "Камень, ножницы, бумага" между пользователем и компьютером.
# Компьютер должен делать случайный выбор (камень, ножницы или бумага).
# Пользователь должен ввести свой выбор.
# Определите победителя и выведите результат.

import random


def computer_choice() -> str:
    options = ["камень", "ножницы", "бумага"]
    return random.choice(options)


def winner(computer: str, user: str) -> int:
    if computer == user:
        return 0
    elif (computer == "камень" and user == "ножницы") or \
            (computer == "ножницы" and user == "бумага") or \
            (computer == "бумага" and user == "камень"):
        return 1
    else:
        return 2


def play_game():
    print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")

    while True:
        user = input("Введите ваш выбор (камень, ножницы, бумага): ").lower()
        if user not in ["камень", "ножницы", "бумага"]:
            print("Ошибка: Некорректный ввод. Попробуйте ещё раз.")
            continue

        computer = computer_choice()
        print(f"Компьютер выбрал: {computer}")

        result = winner(computer, user)
        if result == 0:
            print("Ничья!")
        elif result == 1:
            print("Компьютер выиграл!")
        else:
            print("Вы выиграли!")

        repeat = input("Хотите сыграть ещё раз? (да/нет): ").lower()
        if repeat != "да":
            print("Спасибо за игру!")
            break


play_game()
