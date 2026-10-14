import functools


#Задача 1
def caesar_cipher(text, shift):

    result = ""
    for letter in text:
        result += chr(ord(letter) + shift)

    return result
text = "abc z"
shift = 1

print(caesar_cipher(text, shift))

#Задача 2
def analyze_logs(logs):
    all_logs_list = []

    for line in logs:
        user, action, status = line.split(" ")
        logs_dict = {"user": user, "action": action, "status": status}
        all_logs_list.append(logs_dict)
    return all_logs_list

my_logs_list = [
    "ivan LOGIN SUCCESS",
    "anna LOGIN FAILED",
    "ivan LOGOUT SUCCESS",
    "ivan LOGIN FAILED"
]

print(analyze_logs(logs=my_logs_list))

#Задача 3
def return_type(target_type):
    def decorator(func):
        @functools.wraps(target_type)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return target_type(result)
        return wrapper
    return decorator

@return_type(int)
def add_numbers(a, b):
    return a + b
print(type(add_numbers(5, 5)))