#Задача 1
salaris = [50000, 120000, 85000, 45000, 90000]
plan_fulfield = [True, False, True, True, False]

total_budget = 0

for i in range(len(plan_fulfield)):
    if plan_fulfield[i] == True:
       total_budget += salaris[i] * 1.2
    else:
         total_budget += salaris[i]
print(f"Общий оклад сотрудников: {total_budget}")

#Задача 2
transactions = [1200, 45000, 150, 600000, 23000, 850000, 4000]
limit = 100000

approved_trans = []
blocked_trans = []

for i in transactions:
    if i >= limit:
       blocked_trans.append(i)
    else:
        approved_trans.append(i)
print(approved_trans)
print(blocked_trans)

#Задача 3
days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
steps_history = [8500, 12000, 4000, 11000, 7000, 15000, 9500]
daily_norm = 10000


succesful_days = 0
unsuccesful_days = 0

for i in range(len(steps_history)):
    if daily_norm <= steps_history[i]:
        succesful_days += 1
else:
    unsuccesful_days += 1
    print(f"В {days[i]} день норма не выполнена: {steps_history[i]} шагов")

#Задача 4
warehouse = [
    ["Монитор", 2, 15000],
    ["Клавиатура", 15, 2500],
    ["Мышь", 1, 1200],
    ["Коврик", 30, 500],
    ["Наушники", 3, 4000],
]
critical_restock = 5
shopping_list = []
total_cost = 0

for item in warehouse:
    if item[1] < critical_restock:
        shopping_list.append(item)
        total_cost += item[2]

print("Список покупок:", shopping_list)
print("Итоговая сумма для закупки по 1 шт:", total_cost)

#Задача 5
raw_emails = [" user@test.com", "admin@gmail.com ", "USER@test.com ", "invalid_email", "guest@mail.ru"]
valid_emails = []

for i in raw_emails:
    clean_name = i.strip().lower()
    if "@" not in clean_name:
        continue
    if clean_name in valid_emails:
        continue
    valid_emails.append(clean_name)
print(valid_emails)