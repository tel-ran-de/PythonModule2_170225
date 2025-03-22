


def get_code():
    code = input("Введите код : " )


    if len(code) == 16 and code.isdigit():
        print("Номер принят спасибо")
        return code

    else:
        print("ошибка")

        return get_code()

kode = get_code()


#code = int(input("Введите 16 значный номер : "))



#code = [code1]

#for num in code1:
  #  if num  % 2 == 0:

     # print(num)





















