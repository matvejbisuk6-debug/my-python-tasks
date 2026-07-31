#Задача 1
word1 = {"a": 10, "b": 20}
word2 = {"b": 5, "c": 15}

def merge_dicts(d1, d2):
    all_word = {}
    for i in d2:
        if i in all_word:
            all_word[i] += d2[i]
        else:
            all_word[i] = d2[i]
    return all_word
print(merge_dicts(word1, word2))

#Задача 2
word1 = {"ice": "cold", "fire": "hot"}

def invert_dict(d):
    return {value: key for key, value in d.items()}
print(invert_dict(word1))

#Задача 3
product_list = {"milk": 5, "bread": 2, "apple": 12}
min_quality = 5

def filter_products(product, min_quality):
    return {value: value for key, value in product.items() if value >= min_quality}
print(filter_products(product_list, min_quality))

#Задача 4
sort_list = {"apple": 5, "banana": 12, "orange": 5}

def sort_value(d):
    new_sort_list = {}
    pairs = [(-value, key) for key, value in d.items()]
    sorted_pairs = sorted(pairs)
    for value, key in sorted_pairs:
        new_sort_list[key] = -value
    return new_sort_list
print(sort_value(sort_list))

#Задача 5
work = [{"name": "Иван", "departament": "IT", "salary": 100},
        {"name": "Анна", "departament": "HR", "salary": 80},
        {"name": "Петр", "departament": "IT", "salary": 120}
        ]

def deep_get(employees):
    new_work = {}
    for employees in employees:
        name = employees["name"]
        departament = employees["departament"]
        new_work[name] = departament
    return  new_work
print(deep_get(work))




