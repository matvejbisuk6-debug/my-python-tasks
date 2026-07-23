#Задача 1
number = int(input("Введите положительное число: "))
counter = 0

while True:
    number = number // 2
    counter += 1
    if number < 1:
        break
print(counter)

#Задача 2
money = 10000

while True:
    withdraw_money = int(input("Сумма которую хотите ввести: "))
    if withdraw_money == 0:
        break
    if withdraw_money <= money:
        money = money - withdraw_money
        print("Деньги успешно выведены")
    elif withdraw_money > money:
        print("Введите снова")
    if money == 0:
        break

#Задача 3
string = str(input("Введите строку: "))
string.lower()
i = 0
plus = 0

while i < len(string):
    if "a" in string[i]:
        plus += 1
    i += 1
print(plus)

#Задача 4
number = 12345
reversed_number = 0

while number > 0:
    reversed_number = (reversed_number * 10) + (number % 10)
    number = number // 10
print(reversed_number)

#Задача 5
number1 = 20
number2 = 10
delitel = 0

while True:
    delitel += 1
    if number1 > 0 and number2 > 0:
        number1 = number1 - number2
    else:
        number2 = number2 - number1
    break
print(delitel)