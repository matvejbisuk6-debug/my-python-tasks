import functools
import time

#Задача 1
def greeting_decorator(decorator):
    def wrapper():
        print("---Запуск функции---")
        decorator()
        print("---Функция завершена---")
    return wrapper

@greeting_decorator
def say_hello():
    print("Привет, мир!")

say_hello()

#Задача 2
def uppercase_decorator(decorator):
    def wrapper():
        print("hello python")
        decorator()
        print("hello python".upper())
    return wrapper

@uppercase_decorator
def get_text():
    return "hello python"
print(get_text())

#Задача 3
def timer_decorator(decorator):
    @functools.wraps(decorator)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = decorator(*args, **kwargs)
        print()
        end = time.time() - start_time
        print(f"Функция выполнилась за {end:.3f} сек")
        return res
    return wrapper

@timer_decorator
def new_time(sleep, b):
    time.sleep(sleep)
    return sleep + b

print(new_time(1, 0))

#Задача 4
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Аргументы функции:", args, kwargs)
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(a, b):
    if type(a) is int and type(b) is int:
        return "Типы данных верны"
    else:
        return "Ошибка: Допустимы только целые числа"

print(greet(5,"10"))

#Задача 5
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
        print("Некая функция вызвана", args, kwargs)
        return func(*args, **kwargs)
    wrapper.counter = 0
    return wrapper

@my_decorator
def function(name_function):
    return f"Функция {name_function} вызвана {function.counter} раз"

print(function("Функция 1"))

#Задача 6
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Решение начато")
        result = func(*args, **kwargs)
        print("Решение закончено")
        return result
    wrapper.cache = {}
    return wrapper

@my_decorator
def get_data(dict1, value1, key1):
    if key1 not in dict1:
        dict1[key1] = value1
        return dict1
    else:
        return "Значения в кэш не добавлены"

print(get_data({}, 2, "Пока"))