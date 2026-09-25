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