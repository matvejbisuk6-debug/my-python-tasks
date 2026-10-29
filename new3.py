#Задача 1
correct_pin = "4815"
attempts = 0

while True:
    enter_pin = str(input("Введите Пин-код: "))
    attempts += 1
    if enter_pin == correct_pin:
        print("Пароль верен, доступ разрешен!")
        break
    elif attempts >= 3:
        print("Сейф заблокирован, попытки закончились.")
        break
    else:
        print(f"Неправильно, осталось попыток: {attempts}")