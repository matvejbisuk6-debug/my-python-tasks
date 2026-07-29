#Задача 1
price = 599.99
quantity = 3
sum = price + quantity

print(sum)

#Задача 2
seconds = 4000
hours = seconds // 3600
minutes = seconds % 3600 // 60

print(hours)
print(minutes)

#Задача 3
first_name = "Имя"
last_name = "Фамилия"
full_name = first_name + " " + last_name

print(full_name.upper())

#Задача 4
phone = "+7-999-111-22-33"

print(phone.replace("+7-999-111-22-33", "+79991112233"))

#Задача 5
number = int(input("Enter number of apartment: "))
apartment_floor = 4
apartment_number = 20
entarance = (number - 1) // apartment_number + 1
floor = (number - 1) % 20 // 4 + 1
print(number)
print(entarance)
print(floor)

#Задача 6
user_input = "25"
my_int = int(25)
print(my_int + 5)

#Задача 7
pi_str = "3.14159"
pi_float = float(3.14159)
pi_int = int(3.14159)
print(pi_float)
print(pi_int)

#Задача 8
age = 20
is_adult = age >= 18 and age < 65
print(is_adult)

#Задача 9
bool1 = ""
bool2 = " "

print(bool1)

print(bool2)

#Задача 10
a = 42
b = 42.0
c = "42"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
