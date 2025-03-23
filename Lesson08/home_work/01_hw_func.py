# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    ticket_number_str = str(ticket_number)
    str_len = len(ticket_number_str)
    side1 = 0
    side2 = 0
    if str_len % 2 == 0:
        for index, number in enumerate(ticket_number_str):
            if index < str_len/ 2:
                side1 += int(number)
            else:
                side2 += int(number)
        result = f"{ticket_number_str} {'Счастливый' if side1 == side2 else 'неТь'}"
        return result
    else:
        return f"{ticket_number} неТь"

# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(436753))
print(lucky_ticket(4367132))
print(lucky_ticket(1426733))
