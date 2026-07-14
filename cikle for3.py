#Задача 1
temperatures = [18, 22, 15, 20, 17, 23, 19]
for i in temperatures:
    if i > 19:
        print(i)

#Задача 2
numbers = [3, 7, 2, 8, 5]
number2 = []

for i in numbers:
    new_number = 2 * i
    number2.append(new_number)
print(number2)

#Задача 3
grades = [5, 3, 4, 5, 2, 4, 5, 3]
counter = 0

for i in grades:
    if i == 5:
        counter += 1
    print(counter)

#Задача 4
prices = [150, 80, 420, 230, 90]
min_price = 150
max_price = 150

for i in prices:
    if i < max_price:
        max_price = i
    print(max_price)
    if i > min_price:
        min_price = i
    print(min_price)

#Задача 5
users = ["Андрей", "Ольга", "Иван", "Анна", "Дмитрий"]

for i in users:
    if i[0] == "А":
        print(i)