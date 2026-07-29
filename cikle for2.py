#Задача 1
from typing import overload

prices_rub=[1500, 4200, 990, 12000, 450]
usd_rate = 95.5

prices_usd = []

for item in prices_rub:
    new_item = round(item / usd_rate, 2)
    prices_usd.append(new_item)
print(prices_usd)

#Задача 2
exam_scores = [56, 89, 45, 92, 71, 84]
max_score = exam_scores[0]

for i in exam_scores:
    if i > max_score:
        max_score = i
print(max_score)

#Задача 3
first_names = ["Алексей", "Мария", "Иван"]
last_names = ["Петров", "Сидорова", "Иванов"]
full_names = []

for i in range(len(first_names)):
    new_i = first_names[i] + " " + last_names[i]
    full_names.append(new_i)
print(full_names)

#Задача 4
server_loads = [85, 12, 98, 45, 100, 7, 91]
overloaded_count = 0
idle_count = 0

for i in server_loads:
    if i > 80:
        overloaded_count += 1
    if i < 20:
        idle_count += 1
print(overloaded_count)
print(idle_count)

#Задача 5
rpg_inventory = [
    ["Стальной меч", "Оружие"],
    ["Лечебное зелье", "Химия"],
    ["Лук охотника", "Оружие"],
    ["Кожанный щит", "Броня"],
    ["Ядовитая стрела", "Оружие"]
]
weapons_only = []

for i in rpg_inventory:
    if "Оружие" in i[1]:
        weapons_only.append(i[0])
print(weapons_only)