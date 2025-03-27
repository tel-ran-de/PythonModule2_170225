def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        # Код до вызова оригинальной функции
        print("wrapper_function executed this before {}".format(original_function.__name__))

        result = original_function(*args, **kwargs)

        # Код после вызова оригинальной функции
        print("wrapper_function executed this after {}".format(original_function.__name__))
        return result
    return wrapper_function

@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 25)