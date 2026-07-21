#Задача 1
list1 = [1, 12, 29, 44, 57, 72, 85, 94]

def even_numbers(list_numbers):
    result = []
    for i in list1:
        if i % 2 == 0:
            result.append(i)
    return result
print(even_numbers(list1))

#Задача 2
number = int(input("Введите число: "))

while number >= 1:
    print(number)
    number-= 1

#задача 3
while True:
    numbers = []
    number = int(input("Введите число: "))

    if number == 0:
        break

    numbers.append(number)

    list_sum = sum(numbers)
print(list_sum)

#Задача 4
number1 = 7
number2 = 1

while True:
    if number2 == 11:
        break

    score = number1 * number2
    print(f" {number1} * {number2} = {score}")
    number2 += 1

#Задача 5
unknown_number = 42

while True:
    number = int(input("Угадайте число: "))

    if number > unknown_number:
        print("Больше")
    elif number < unknown_number:
        print("Меньше")
    else:
        print("Вы угадали")
    break