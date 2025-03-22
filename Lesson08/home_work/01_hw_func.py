# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.


def lucky_ticket(ticket):
    if ticket[0:1:2] == ticket[-1:-2:-3]:
        print("Вы выйграли")
ticket = int(input("номер билета :"))
    # TODO: your code here



# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))