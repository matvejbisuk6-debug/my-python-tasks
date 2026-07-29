#Задача 1
number = 357
mid_digit = number % 100 // 10
print(mid_digit)

#Задача 2
radius = 7
pi = 3.14159
area = pi * radius ** 2
print(round(area))

#Задача 3
user_login = "  my_cool_login_2026  "
print(len(user_login))
print(user_login.strip())
print(len(user_login.strip()))

#Задача 4
filename = "report.pdf"
print(filename.endswith(".pdf"))

#Задача 5
item = "Ноутбук"
price = 75000
print(f"{item} стоит {price:_}")

#Задача 6
width = length = height = 10
length = 25
volume = width * length * height
print(volume)

#Задача 7
a = 10 / 5
b = 10 // 5
print(a)
print(b)

#Задача 8
message = "ВНИМАНИЕ! Вы выиграли бесплатный приз! Кликните тут."
has_spam = "приз" in message
print(has_spam)

#Задача 9
num1 = 2.5
num2 = 3.5
print(round(num1))
print(round(num2))

#Задача 10
compare_res = "apple" > "Apple"
print(compare_res)
