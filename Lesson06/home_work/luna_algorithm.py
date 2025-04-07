


def get_code():
    while True:
        code = input("Введите код : " )


        if len(code) == 16 and code.isdigit():
            print("Номер принят спасибо")
            return code

        else:
            print("Ошибка")





kode = get_code()
if kode:
    koderevers = list(map(int, kode[::-1]))





    for i in range(len(koderevers) - 2, -1, -2):
        koderevers[i] *= 2
        if koderevers[i] > 9:
            koderevers[i] -= 9

    totals = sum(koderevers)
    is_valid = totals % 10 == 0
    totals1 = totals % 10






    print("Обработанный список",koderevers)
    print("Сумма  чисел последовательности",totals)
    print("Проверочная цифра", totals1)
    print("Код верен." if is_valid else "Код некорректен.")












































