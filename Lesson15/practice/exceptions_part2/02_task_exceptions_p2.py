def validate_email(email):
    # Добавьте проверку, что email содержит символ '@'.
    # Если email некорректный, выбросьте исключение ValueError.
<<<<<<< HEAD
    if "@" not in email:
        raise ValueError("Email is not valid")

=======
    if '@' not in email:
        raise ValueError("Некорректный email")
>>>>>>> 6defc2976e31c90e2919ec1b8f35a104ee59242d
    return email


# Добавьте обработку исключения ValueError
try:
    print(validate_email("user.example.com"))
except ValueError as e:
<<<<<<< HEAD
    print(e)
=======
    print(e)
>>>>>>> 6defc2976e31c90e2919ec1b8f35a104ee59242d
