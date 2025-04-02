# Задача "Игра "Камень, ножницы, бумага"

# Создайте функцию, которая имитирует игру "Камень, ножницы, бумага" между пользователем и компьютером.
# Компьютер должен делать случайный выбор (камень, ножницы или бумага).
# Пользователь должен ввести свой выбор.
# Определите победителя и выведите результат.
import random

def computer_choice():
    return random.choice(["камень", "ножницы", "бумага"])

def winner(comp_choice: str, pl_choice: str) -> int:
    """
    :return: 1 - comp 2 - player
    """
    ...
    if comp_choice == "бумага" and pl_choice == "камень":
        return 1
    else:
        return 2

# player
turn = 0
while True:
    if turn == 5:
        break
    player_choice = input("Введите камень, ножницы или бумага: ")
    comp_choice = computer_choice()
    print(f"Компьютер выбрал: {comp_choice}")
    if winner(comp_choice, player_choice) == 1:
        print("Win computer")
    else:
        print("Win player")

    turn += 1


