#Задача 1
max_price = 15000
alowed_airlines = ["Аэрофлот", "S7", "Emirates"]
requires_baggage = True

ticket_price = 13500
ticket_airline = "Победа"
ticket_has_baggage = True

if (ticket_price <= max_price and
    ticket_airline in alowed_airlines and
        (not requires_baggage or ticket_has_baggage)):
             print("Билет подходит")

else:
    print("Билет не подходит")

#Задача 2
min_secure_balance = 500
suspicious_adresses = ["0xBad1", "0xScam99", "0xHackX"]

user_balance = 1200
user_last_transactions = ["0xAbc2", "0xScam99", "0xScam99", "0xXyz4"]

has_scam_tx = bool(set(user_last_transactions).intersection(set(suspicious_adresses)))

if  min_secure_balance > user_balance or has_scam_tx:
    status = "Заблокирован"
else:
    status = "Одобрен"
print(status)

#Задача 3
free_vip_tables = 2
free_regular_tables = 0

guest_count = 5
has_gold_card = True

if has_gold_card == True and free_vip_tables - 1 >= 0:
    print("Добро пожаловать в VIP зал")
elif free_regular_tables - 1 >= 0:
    print("Стол в общем зале забронирован")
else:
    print("Извините, свободных мест нет")

#Задача 4
forbidden_items = ["оружие", "алкоголь", "жидкости вейп"]

parcel_items = ["ноутбук", "чехол", "алкоголь"]
parcel_weight = 22
parcel_item = 180

if forbidden_items in parcel_items:
    status = "Конфисковано"
    fee = 0
else:
    status = "Посылка разрешена"
    if parcel_weight <= 20 or parcel_item <= 180:
        fee = 0
    else:
        fee = 25

print(status)
print(f"Итоговый размер пошлины: {fee}")

#Задача 5
inventory = ["Железо", "Дерево", "Огненный камень", "Зелье"]
max_stols = 5
recipe = ["Железо", "Огненный камень"]

if set(recipe).issubset(set(inventory)):
    inventory.remove("Железо")
    inventory.remove("Огненный камень")
    if len(inventory) + 1 <= max_stols:
        inventory.append("Огненный меч")
        print("Крафт успешен")
        print(inventory)
else:
    print("Не хватает ресурсов")