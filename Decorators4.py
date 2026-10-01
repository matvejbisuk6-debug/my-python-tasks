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
def strip_strings(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result = result.strip()
        return result
    return wrapper

@strip_strings
def correct_text():
    return " Hello world "

print(correct_text())

#Задача 4
def allow_roles(dict):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result not in dict:
                return True
            else:
                return False
        return wrapper
    return decorator

@allow_roles(["admin", "editor"])
def check_roles(role):
    return role

print(check_roles("programmer"))

#Задача 5
def register_action(command_name):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            commands = {}
            commands[command_name] = func
            print(commands)
            return result
        return wrapper
    return decorator

@register_action("/start")
def start_bot():
    return "Приветствие"

print(start_bot())