def check_age(age):
    try:
        if age > 0:
            return age
    except ValueError:
        return None

    # Добавьте проверку, что возраст должен быть положительным числом.
    # Если возраст некорректный, выбросьте исключение ValueError.
<<<<<<< HEAD


print(check_age(-5))
=======
    if age < 0:
        raise ValueError("Возраст не может быть отрицательным")
    return age

print(check_age(5))
>>>>>>> 6defc2976e31c90e2919ec1b8f35a104ee59242d
