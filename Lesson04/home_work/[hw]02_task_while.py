n = int(input("Количество карточек: "))  # n = 5 |1|2|3|4|5| S1=15
# i = 0
# all_card_sum = 0
# while i < n:
#     i += 1
#     all_card_sum += i
all_card_sum = n * (n + 1) // 2
# Цикл, который выполнится n-1 раз

i = 0
rest_card_sum = 0
while i < n - 1:
    card_number = int(input("Номер карточки: "))  # |3|1|4|5| S2=13
    rest_card_sum += card_number
    i += 1

print("Номер потерянной карточки:", all_card_sum - rest_card_sum)
