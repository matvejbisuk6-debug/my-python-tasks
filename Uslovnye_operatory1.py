#Задача 1
height = 139
if height >= 140:
    print("Доступ разрешен")
else:
    print(f"Доступ запрещен, не хватает {140 - height}")

#Задача 2
order_sum = 2500
if order_sum > 5000:
    print(f"Доставка бесплатная, от 0 рублей {order_sum}")
elif order_sum > 2000:
    print(f"Доставка 200 рублей, плати {order_sum + 200} рублей")
else:
    print(f"Стоимость доставки 400 рублей, плати {order_sum + 400} рублей")

#Задача 3
age = 22
has_income = True
if age > 21 and has_income == True:
    print("Кредит одобрен")
else:
    print("В кредите отказано")

#Задача 4
login = "admin"
password = "secret123"
if login == "admin" and password == "secret123":
    print("Верный логин, добро пожаловать!")
else:
    print("Неверный логин, иди нахуй")

#Задача 5
number = -7
result = "Положительное" if number >= 0 else "Отрицательное"
print(result)

#Задача 6
is_premium = False
has_promo = True
is_open = True
if is_premium == True or has_promo == True and is_open == True:
    print("Скидка активирована")
else:
    print("Скидка не предоставляется, извените")

#Задача 7
year = 2026
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"Год {year} - високосный")
else:
    print(f"Год {year} - обычный")

#Задача 8
subject = "Вопрос по оплате подписки"
if "оплат" in subject.lower() or "счет" in subject:
    print("Напрвить в финансовый отдел")
elif "пароль" in subject.lower() or "логин" in subject:
    print("Направить в техподдержку")
else:
    print("Направить в общий отдел")

#Задача 9
bmi = 22.5
if bmi < 18.5:
    print("Недостаточный вес")
elif bmi < 25:
    print("Норма")
elif bmi < 30:
    print("Избыточный вес")
else:
    print("Ты жиртрест")

#Задача 10
http_status = 404
match http_status:
    case 200:
        print("OК")
    case 404:
        print("Страница не найдена")
    case 500:
        print("Ошибка сервера")
    case _:
        print("Неизвестный статус")



