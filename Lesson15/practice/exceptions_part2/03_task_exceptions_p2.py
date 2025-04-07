def check_string_length(text, min_length):
    if len(text) < min_length:
        print("String is OK")
    else:
        raise ValueError("String is too short")

    # Добавьте проверку, что длина строки не меньше min_length.
    # Если строка слишком короткая, выбросьте исключение ValueError.
    return text


# Добавьте обработку исключения ValueError
print(check_string_length("abc", 5))
