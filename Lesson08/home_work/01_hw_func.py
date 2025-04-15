# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
from zoneinfo import reset_tzpath

from unicodedata import digit


def lucky_ticket(ticket):
     ticket = str(ticket)
     if len(ticket) != 6:
       return False

     ticket1 = ticket[:3]
     ticket2 = ticket[3:]

     ticket1_sum = sum(int(digit) for digit in ticket1)
     ticket2_sum = sum(int(digit) for digit in ticket2)
     return ticket1_sum == ticket2_sum

ticket = int(input("ВВедите 6 значный номер билета :"))

if lucky_ticket(ticket):
    print("Билет счастливый !!!")
else:
    print("Билет не счастливый")





    # TODO: your code here



# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))