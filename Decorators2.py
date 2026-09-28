import functools
import json
import time
from turtledemo.penrose import start


#Задача 1
def to_json(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        start_dict = json.dumps(result)
        return start_dict
    return wrapper

@to_json
def get_user_data():
    return {"name": "Alex", "age": 25}

print(get_user_data())

#Задача 2
def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if "хорошо" in result:
            return result
        else:
            return result.replace("Плохо", "*****")
    return wrapper

@decorator
def check_func(string):
    return string

print(check_func("Функция выполнена хорошо"))
print(check_func("Функция выполнена плохо, переделай"))

#Задача 3
def log_args(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Вызов функции {func.__name__} с аргументами {args} и {kwargs}")
        print(f"Результат функции: {result}")
        return result
    return wrapper

@log_args
def my_func(a, b, status="active"):
    my_dict = {"status": status}
    return my_dict

my_func(1, 2, status="active")

#Задача 4
def require_admin(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        user_dict = args[0]
        if user_dict.get("role") == "admin":
            return func(*args, **kwargs)
        else:
            return "Доступ запрещен: требуется роль admin!"
    return wrapper

@require_admin
def check_admin(dict):
    return dict

print(check_admin({"name": "Иван", "role": "user"}))
print(check_admin({"name": "Иван", "role": "admin"}))

#Задача 5
def delay_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time() - start_time
        print(f"Функция выполнилась за {end_time:.3f} сек")
        return result
    return wrapper

@delay_decorator
def check_time(sleep):
    time.sleep(2)
    return sleep

print(check_time(2))