#Задача 1
from Uslovnye_operatory1 import password

data = 5
if type(data) == str:
    print("Получена строка")
elif type(data) == int:
    print(f"Возваодим число {data} и получаем {data ** 2}")

#Задача 2
password = "Qwerty123"
if len(password) >= 6 and any(char.isdigit() for char in password):
    print("Надежный пароль")
else:
    print("Пароль слишком слабый")

#Задача 3
status = "none"
purchase_amount = 2500
if status == "gold":
    print(f"Вам предоставляется скидка 15% и итоговая сумма покупки - {purchase_amount - purchase_amount * 0.15}")
elif status == "silver" and purchase_amount < 5000:
    print(f"Вам предоставляется скидка 10% и итоговая сумма покупки - {purchase_amount - purchase_amount * 0.10}")
elif purchase_amount >= 5000 and status == "silver":
    print(f"Вам предоставляется скидка 12% и итоговая сумма покупки - {purchase_amount - purchase_amount * 0.12}")
elif status == "none" and purchase_amount >= 10000:
    print(f"Вам предоставляется скидка 20% и итоговая сумма покупки - {purchase_amount - purchase_amount * 0.20}")
else:
    print("Скидка составляет 0%")

#Задача 4
temperature = 25
weather_report = "Жарко" if temperature >= 30 else "Тепло" if temperature > 15 else "Холодно"
print(weather_report)

#Задача 5
start1 = 9
end1 = 12
start2 = 11
end2 = 15
if max(start1, start2) < min(end1, end2):
    print("Пересечение есть, созвон есть")
else:
    print("Времени для созвона нема")

#Задача 6
color = "green"
is_emergency_venicle_approaching = False
if is_emergency_venicle_approaching == True:
    print("Остановится и пропустить спецтранспорт")
elif color == "green":
    print("Ехать")
elif color == "yellow":
    print("Приготовиться")
else:
    print("Стоять")

#Задача 7
month = 2
day = 30
if day <= 30 and month in [4, 6, 9, 11]:
    print("Дата корректна")
elif month in [1, 3, 5, 7, 8, 10, 12] and day <= 31:
    print("Дата корректна")
elif day <= 28 and month == 2:
    print("Дата корректна")
else:
    print("Несуществующая дата")

#Задача 8
banned_words = ["скам", "крипта", "выигрыш"]
comment = "Посмотри на этот выигрыш"
if "скам" in comment or "крипта" in comment or "выигрыш" in comment:
    print("Комментарий заблокирован")
else:
    print("Комментарий опубликован")

#Задача 9
age = 15
is_student = True
if age <= 6:
    print("0 рублей, бесплатный")
elif age <= 18 and is_student == True:
    print(f"{300 - 300 * 0.5} рублей, вам положена скидка")
elif age <= 18:
    print("300 рублей")
elif age <= 19 and is_student == True:
    print(f"{600 - 600 * 0.2} рублей, вам положена скидка")
elif age <= 19:
    print("600 рублей")

#Задача 10
sms_sent = True
email_sent = False
if sms_sent == True and email_sent == True or sms_sent == False and email_sent == False:
    print("Ошибка системы")
else:
    print("Код отправлен успешно")