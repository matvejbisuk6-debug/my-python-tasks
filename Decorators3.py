import functools
import time


#Задача 1
def wrap_in_tag(tag_name):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            html_tag = f"<{tag_name}>{result}</{tag_name}>"
            return html_tag
        return wrapper
    return decorator

@wrap_in_tag("div")
def text_gen():
    return "Привет"

print(text_gen())

#Задача 2
def check_str(check):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if "password" in result:
                return f"{check} успешно настроен, вы молодец!"
            else:
                return "Ничего не настроено попробуйте попытку снова"
        return wrapper
    return decorator

@check_str("******")
def correct_text(string):
    return string

print(correct_text("password успешно настроен, вы молодец!"))

#Задача 3
def repeat(num):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for _ in range(num):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Привет!")

greet()

#Задача 4
def numbers(num):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if num in result:
                return result
            else:
                return "Value error, значение вне диапазона!"
        return wrapper
    return decorator

@numbers(2)
def check_numbers(a, b):
    return a, b

print(check_numbers(1, 2))

#Задача 5
def cache(seconds):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            new = time.time() - start_time
            if new > seconds:
                return f"Внимание: функция выполнялась долго ({new:.2f} сек)!"
            time_data = (start_time, new)
            return result + time_data
        return wrapper
    return decorator

@cache(2)
def check_time(tuple):
    time.sleep(0.5)
    return tuple

print(check_time(("Иван", "активен")))
