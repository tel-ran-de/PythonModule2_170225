def validate_email(email):
    # Добавьте проверку, что email содержит символ '@'.
    # Если email некорректный, выбросьте исключение ValueError.
    if '@' not in email:
        raise ValueError("Некорректный email")
    return email

# Добавьте обработку исключения ValueError
try:
    print(validate_email("user.example.com"))
except ValueError as e:
    print(e)