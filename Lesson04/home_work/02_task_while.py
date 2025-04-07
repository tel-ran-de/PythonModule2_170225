

n = int(input("Количество карточек: "))
# Цикл, который выполнится n-1 раз
sum1 = sum(range(1, n + 1))
card = 0

count = 0

while count < n - 1:
    card_number = int(input("Номер карточки: "))
    card += card_number
    count += 1

lost_card = sum1 - card
print("Номер потерянной карточки:",lost_card )
