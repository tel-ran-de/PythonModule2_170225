def check_age(age):
    try:
        if age > 0:
            return age
    except ValueError:
        return None

    # Добавьте проверку, что возраст должен быть положительным числом.
    # Если возраст некорректный, выбросьте исключение ValueError.


print(check_age(-5))
