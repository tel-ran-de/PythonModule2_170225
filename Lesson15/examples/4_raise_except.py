def check_status(status):
    if status == "OK":
        return "Все в порядке"
    elif status == "WARNING":
        # Выбрасываем исключение
        raise Warning(f"Предупреждение: {status}")
    elif status == "ERROR":
        raise RuntimeError(f"Ошибка: {status}")
    else:
        raise ValueError(f"Неизвестный статус: {status}")


# Обрабатываем исключение
try:
    result = check_status("WARNING")
    print("Результат:", result)
except Warning as w:
    print(f"Предупреждение: {w}")
except RuntimeError as e:
    print(f"Ошибка: {e}")
except ValueError as v:
    print(f"Ошибка ввода: {v}")

try:
    result = check_status("UNKNOWN")
    print(result)
except ValueError as v:
    print(f"Ошибка ввода: {v}")

try:
    result = check_status("OK")
    print(result)
except Exception as e:
    print(f"Ошибка: {e}")
