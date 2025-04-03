import random

def mult_3(number):
    return number % 3 == 0

def dice_roll():
    return random.randint(1, 6)

def generate_password(password_length: int) -> str:
    chars = ([chr(code) for code in range(ord("A"), ord("Z"))]
             + [chr(code) for code in range(ord("a"), ord("z"))]
             + [chr(code) for code in range(ord("0"), ord("9"))]
             + ["@", "!", "#"])

    password = ""
    for _ in range(password_length):
        password += random.choice(chars)

    return password

if __name__ == "__main__":
    print(generate_password(6))
    print(generate_password(4))
    print(generate_password(5))