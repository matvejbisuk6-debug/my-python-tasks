#задача 1
N = int(input("Введите целое число: "))
score = 2
count = 2

while True:
    i = score ** count
    if N > i:
        print(i)
        count += 1
    else:
        break

#Задача 2
while True:
    age = int(input("Введите свой возраст"))
    if age <= 0 or age > 120:
        print("Предупреждение")
    else:
        print("Возраст введен правильно")
    break

#Задача 3
X = int(input("Введите число: "))
A = 0
B = 1

while True:
    A, B = B, A + B
    if  B > X:
        print(B)
    break

#Задача 4
A = int(input("Введите целое число: "))
total_sum = 0

while A > 0:
    sum += A % 10
    A = A // 10
print(total_sum)

#Задача 5
contribution = 1000000
percents = 0.10
size = 10000000
counter_years = 0

while True:
    money_in_year = contribution * percents
    contribution += money_in_year
    if contribution <= size:
        counter_years += 1
    if contribution >= size:
        break
print(counter_years)