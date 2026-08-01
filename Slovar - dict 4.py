#Задача 1
from peremennye2 import result

d = {"user":  {"profile": {"age": 25}}}
path = "user.profile.age"

def deep_get(d, path):
    keys = path.split(".")
    for key in keys:
        if key in d:
           d = d[key]
        else:
            return None
    return d
print(deep_get(d, path))

#Задача 2
dict1 = {"app": {"port": 8080, "host": "localhost"}, "debug": True}
dict2 = {"app": {"port": 9000, "logging": "info"}, "version": 1.0}

def new_dict(dict1, dict2):
    result1 = dict1.copy()
    for key in dict2:
        if key in result1 and isinstance(result1[key], dict) and isinstance(dict2[key], dict):
            result1[key] = new_dict(result1[key], dict2[key])
        else:
            result1[key] = dict2[key]
    return result1
print(new_dict(dict1, dict2))

#Задача 3
product = {"хлеб": 50, "молоко": 120, "сыр": 350, "Яблоки": 120}

def max_price(products):
    return max(products, key = products.get)
print(max_price(product))

#Задача 4
data = {"name": "Alex", "age": 25}
mapping = {"name": "имя"}

def rename_keys(data, mapping):
    new_list = {}
    for key, value in data.items():
        if key in mapping:
            new_list[mapping[key]] = value
        else:
            new_list[key] = value
    return new_list
print(rename_keys(data, mapping))

#Задача 5
b = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}

def unique_values_dict(b):
    res = {}
    seen = set()
    for key, value in b.items():
        if value in seen:
            continue
        seen.add(value)
        res[key] = value
    return res
print(unique_values_dict(b))