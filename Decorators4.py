import functools
import time

#Задача 1
def format_output(separator):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            line = separator * 20
            middle = result.center(20, separator)
            print(line)
            print(middle)
            print(line)
        return wrapper
    return decorator

@format_output("-")
def get_title():
    return "Главное меню"

print(get_title())

#Задача 2
def cooldawn(seconds):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            wrapper.last_call = 0
            start_time = time.time()
            result = func(*args, **kwargs)
            if start_time > wrapper.last_call and start_time >= seconds:
                return f"Функция успешно запустилась за {start_time} сек!{result}"
            else:
                return "Подождите функция временно недоступна!"
        return wrapper
    return decorator

@cooldawn(2)
def time_check():
    return "Вы получили секретные данные"

print(time_check())

#Задача 3
