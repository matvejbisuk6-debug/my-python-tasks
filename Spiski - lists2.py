#Задача 1
logs = ["192.168.1.1", "10.0.0.1", "192.168.1.1", "172.16.0.1", "192.168.1.1"]
count = logs.count("192.168.1.1")
clear = logs.clear()
print(count)
print(clear)

#Задача 2
players = ["Анна", "Влад", "Диана", "Егор"]
del players[1]
print(players)

#Задача 3
prices_usd = [10, 25, 50, 100]
prices_eur = [price * 0.9 for price in prices_usd]
print(prices_eur)

#Задача 4
notifications = []
if notifications:
    print("У вас есть непрочитанные сообщения!")
else:
    print("У вас нет новых уведомлений")

#Задача 5
scores = [85, 92, 78, 99, 64]
sorted_scores = sorted(scores)
print(scores)
print(sorted_scores)

#Задача 6
ages = [14, 25, 17, 34, 18, 45, 12]
adults = [ad for ad in ages if ad >= 18]
newest = sorted(adults)
print(adults)
print(newest)

#Задача 7
numbers = [1, 2, 3, 4, 5]
numbers[1:4] = [20, 30, 40]
print(numbers)

#Задача 8
emails = ["user@test.com", "admin@test.com", "user@test.com", "guest@test.com", "admin@test.com"]
print(set(list(emails)))

#Задача 9
