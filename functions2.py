#Задача 1
from functions1 import new_list
from peremennye2 import discount

passwords = str(input("Введите пароль: "))

def check_password(password):
        if len(password) >= 8:
            return "Сильный пароль"
        if len(password) <= 8:
            return "Слабый пароль"
print(check_password(passwords))

#Задача 2
spisok = [3, 7, 1, 9, 4, 0]
element = 0

def contains_element(my_list, element):
    for item in my_list:
        if item == element:
            return True
    return False
print(contains_element(spisok, element))

#Задача 3
string = ["а", "бв"]

def double_string(words):
    new_string = []
    for word in words:
        new_list.append(word * 2)
    return new_list
print(double_string(string))

#Задача 4
spisok1 = [1, 18, 74, 25, 93]
spisok2 = [1, 13, 74, 29, 89]

def merge_lists(list1, list2):
    new_list = []
    for i in list1:
        if i not in new_list:
            new_list.append(i)
    for i in list2:
        if i not in new_list:
            new_list.append(i)
        return new_list
print(merge_lists(spisok1, spisok2))

#Задача 5
prices = [75, 200, 500, 20, 800, 1000]
discount_prices = 0.35

def apply_discount(prices, discount_prices):
    new_spisok = []
    for i in prices:
            new_price = i - (i * discount_prices)
            new_spisok.append(new_price)
    return new_spisok
print(apply_discount(prices, discount_prices))
