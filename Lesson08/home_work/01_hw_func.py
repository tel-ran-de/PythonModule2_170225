# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    #
    num_str = str(ticket_number).zfill(6)  # добавляем нули слева, если меньше 6 цифр
    first_half = sum(int(d) for d in num_str[:3])
    second_half = sum(int(d) for d in num_str[3:])
    return first_half == second_halfTODO: your code here
    pass
    

# Тестируем функцию
print(lucky_ticket(123006)) 
print(lucky_ticket(12321))
print(lucky_ticket(436751))
