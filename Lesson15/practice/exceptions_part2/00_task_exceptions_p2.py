# Задача: Добавьте обработку исключения на билет с неверной длиной
def lucky_ticket(ticket_number):
    ticket_str = str(ticket_number)
    if len(ticket_str) != 6:
        raise ValueError("Некорректная длина билета")

    first_half = sum(int(digit) for digit in ticket_str[:3])
    second_half = sum(int(digit) for digit in ticket_str[3:])

    return first_half == second_half


ticket = int(input("Введите шестизначный номер билета: "))

if lucky_ticket(ticket):
    print("Счастливый билет")
else:
    print("Не счастливый билет")
