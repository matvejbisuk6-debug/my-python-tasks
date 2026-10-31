#Задача 1
def calculate_delivery(weight, distance):
    if distance < 10:
        return "Базовая цена 200 рублей"
    elif distance > 10 and distance < 50:
        return "Базовая цена = 200 рублей"
    else:
        return "Базовая цена 700 рублей"
