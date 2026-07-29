#Задача 1
carts = []
carts.append("ноутбук")
carts.append("мышь")
carts.append("наушники")
carts.remove("мышь")
print(len(carts))
print(carts)

#Задача 2
grades = [4, 5, 3, 4, 2, 5]
score1 = grades[0]
score2 = grades[-1]
grades[4] = 5
print(f"Первая оценка - {score1}, вторая - {score2}")
print(grades)

#Задача 3
days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
workdays = days[:5]
weekend = days[5:]
second = days[::2]
print(workdays)
print(weekend)
print(second)

#Задача 4
runners = ["Анна", "Игорь", "Ольга", "Максим", "Дмитрий"]
name = "Ольга" in runners
place1 = runners.index("Максим")
runners.sort()
print(name)
print(f"Максим занял {place1 + 1} место")
print(runners)

#Задача 5
expences = [1200, 550, 3100, 0, 850, 1400, 2300]
print(max(expences))
print(min(expences))
print(sum(expences))
print(sum(expences)/ 7)

#Задача 6
todo = ["Помыть посуду", "Сделать зарядку", "Почитать книгу"]
todo.insert(0,"Позвонить маме")
done_task = todo.pop()
work = ["Ответить на почту", "Написать отчет"]
todo.extend(work)
print(done_task)
print(todo)

#Задача 7
team_a = ["Алексей", "Никита", "Матвей"]
team_b = ["Ольга", "Ирина", "Елена"]
all_players = team_a + team_b
points = [0] * 5
print(all_players)
print(points)

#Задача 8
tags_str = "python, programming, code, backend"
tags_list = tags_str.split(", ")
public_tags = "#".join(tags_list)
print(tags_list)
print(public_tags)

#Задача 9
warehouse = [
    ["Ноутбук", 5, 50000],
    ["Мышь", 20, 1200],
    ["Монитор", 8, 15000]
]
quantity = warehouse[1][1]
common_price = warehouse[2][1] * warehouse[2][2]
print(f"На складе {quantity} мышек")
print(f"Общая стоимость мониторов {common_price} рублей")

#Задача 10
list_a = [1, 2, 3]
list_b = list_a.copy()
list_b.append(4)

print(list_a)
