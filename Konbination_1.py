#Задача 1
blacklist = ["Скам", "Крипта", "Выигрыш", "Акция"]
comment = "Эй! Заходи к нам, тут классная Акция и гарантированный выигрыш"
limit = 10

if len(comment) < limit:
    print("Отклонено, текст слишком короткий")
elif any(word in comment for word in blacklist):
    print("Заблокировано, спам")
else:
    print("Одобрено")

#Задача 2
cart_prices = [1200, 3500, 800]
promo_code = "Step_by_Step"
valid_promos = ["Start", "Step_by_Step", "Python2026"]
subtorial = sum(cart_prices)

if promo_code in valid_promos:
    final_discount = subtorial * 0.10
else:
    final_discount = 0

if subtorial - final_discount >= 4000:
    delivery = 0
else:
    delivery = 300

total = subtorial - final_discount + delivery
print(total)

#Задача 3
group = ["Алексей", "Мария", "Иван"]
new_student = "Ольга"
student_code = 85
item_count = len(group)

if item_count < 4:
    if student_code >= 80:
        group.append(new_student)
        print("Студента успешно зачислен")
        print(group)
    else:
        ("Мест в группе больше нету")
else:
    print("Недостаточно баллов для заичления")

#Задача 4
vip_list = ["Илон Маск", "Джефф Безос"]
regular_list = ["Марк Цукерберг", "Стив Возняк"]
blacklist = ["Билл Гейтс"]

guest_name = "Билл Гейтс"

if guest_name in blacklist:
    print("Отказ, доступ заблокирован службой безопастности!")
elif guest_name in vip_list:
    print("Проходите в VIP-ложу, добро пожаловать!")
elif guest_name in vip_list:
    print("Доступ разрешен в общий зал")
else:
    print("Ошибка, билет не найден в базе данных")

#Задача 5
user_habbit = "Утренняя зарядка"
habbit_story = [True, True, True, False, True, True, True]

if all(habbit_story):
    print(f"Идеально! Вы перевыолнили привычку {user_habbit} каждый день")
elif any(habbit_story):
     Y = habbit_story.count(True) / len(habbit_story) * 100
     print(f"Привычка выполнена на {Y}%")
else:
    print(f"Внимание! Вы забросили привычку {user_habbit}. Пора возвращаться!")