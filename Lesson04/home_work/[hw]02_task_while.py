n = int(input("Количество карточек: "))
# Цикл, который выполнится n-1 раз
full_sum = n * (n + 1) // 2
i = 0

while n > 1:
    card_number = int(input("Номер карточки: "))
    i += card_number
    n -= 1

lost_card = full_sum - i
print(f"Номер потерянной карточки:", lost_card)
