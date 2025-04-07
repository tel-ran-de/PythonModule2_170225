def validate_email(email):
    # Добавьте проверку, что email содержит символ '@'.
    # Если email некорректный, выбросьте исключение ValueError.
    return email

# Добавьте обработку исключения ValueError
print(validate_email("user.example.com"))