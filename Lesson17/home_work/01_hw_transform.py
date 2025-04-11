# У вас есть список цен товаров.
# Вам нужно применить скидку в 10% к каждому товару, цена которого превышает 100 единиц, и вывести новые цены.


prices = [50, 120, 80, 150, 90, 200]

prices_100 = list(filter(lambda x: x > 100, prices))
prices_new = list(map(lambda x: x * 1.1, prices_100))

print(prices_new)
