# Задача "Генерация случайного пароля"
# Создайте строку, содержащую символы разных регистров, цифры и спецсимволы.
# Используйте функцию random.choice() для выбора случайных символов из этой строки.
# Сгенерируйте пароль заданной длины.
import random


def generate_password(password_length: int) -> str:
    chars = ([chr(code) for code in range(ord("A"), ord("Z"))]
             + [chr(code) for code in range(ord("a"), ord("z"))]
             + [chr(code) for code in range(ord("0"), ord("9"))]
             + ["@", "!", "#"])

    password = ""
    for _ in range(password_length):
        password += random.choice(chars)

    return password


print(generate_password(4))
print(generate_password(10))
print(generate_password(6))
