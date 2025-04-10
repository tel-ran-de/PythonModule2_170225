def divide(a, b):
    """Делит a на b."""
    return a / b


def test_divide():
    """Тестирует функцию divide."""
    assert divide(10, 2) == 5.0, "Тест 1 провален: 10 / 2 должно быть 5.0"
    assert divide(6, 3) == 2.0, "Тест 2 провален: 6 / 3 должно быть 2.0"
    assert divide(-4, 2) == -2.0, "Тест 3 провален: -4 / 2 должно быть -2.0"
    assert divide(5, 1) == 5.0, "Тест 4 провален: 5 / 1 должно быть 5.0"
    assert abs(divide(1, 3) - 0.333333333) < 1e-7, "Тест 5 провален: 1 / 3 должно быть приблизительно 0.333..."
    print("Все тесты для функции divide пройдены!")


def multiply(x, y):
    """Умножает x на y."""
    return x * y


def test_multiply():
    """Тестирует функцию multiply."""
    assert multiply(2, 3) == 6, "Тест 1 провален: 2 * 3 должно быть 6"
    assert multiply(-1, 5) == -5, "Тест 2 провален: -1 * 5 должно быть -5"
    assert multiply(0, 10) == 0, "Тест 3 провален: 0 * 10 должно быть 0"
    print("Все тесты для функции multiply пройдены!")


# Запуск тестов
test_divide()
test_multiply()
