# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    # TODO: your code here
    ticket_str = str(ticket_number)

    if len(ticket_str) != 6:
        return False

    first_3_sum = sum(int(digit) for digit in ticket_str[:3])
    second_3_sum = sum(int(digit) for digit in ticket_str[3:])

    return first_3_sum == second_3_sum


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
