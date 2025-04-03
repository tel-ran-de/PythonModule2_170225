# Задача "Генерация случайного пароля"
# Создайте строку, содержащую символы разных регистров, цифры и спецсимволы.
# Используйте функцию random.choice() для выбора случайных символов из этой строки.
# Сгенерируйте пароль заданной длины.
import random


def generate_password(password_length: int) -> str:
<<<<<<< HEAD
    chrs = ([chr(code) for code in range(ord("A"), ord("Z"))] +
            [chr(code) for code in range(ord("a"), ord("z"))] +
            ["!", "@", "#", "$", "%", "^", "&", "*", ] +
            [chr(code) for code in range(ord("1"), ord("9"))])

    password = ""
    for i in range(password_length):
        password += random.choice(chrs)
    return password


print(generate_password(10))
print(generate_password(20))
print(generate_password(30))
=======
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
>>>>>>> 4f7cf1bf3d2dc2459cdaff08dc9316c53615f96f
