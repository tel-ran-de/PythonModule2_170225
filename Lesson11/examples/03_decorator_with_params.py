import time


def timer2(steps):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            # Код до вызова оригинальной функции
            total_time = 0
            for _ in range(steps):
                start = time.time()
                result = original_function(*args, **kwargs)
                end = time.time()
                total_time += end - start
            print(f"среднее время работы функции {total_time / steps}")
            # Код после вызова оригинальной функции
            return result

        return wrapper_function

    return decorator_function


@timer2(10)
def my_function():
    time.sleep(0.5)
    print("Функция выполнена")

my_function()