def check_age(age):
    # Добавьте проверку, что возраст должен быть положительным числом.
    # Если возраст некорректный, выбросьте исключение ValueError.
    if age < 0:
        raise ValueError("Возраст не может быть отрицательным")
    return age

print(check_age(5))