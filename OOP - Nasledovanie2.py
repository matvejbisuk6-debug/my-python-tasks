#Задача 1
class Light:
    def __init__(self, is_on=True):
        self.is_on = is_on

    def turn_on(self):
        if self.is_on == True:
           return "Лампа включена"
        else:
            return "Лампа выключена"

class Smart_Light(Light):
    def __init__(self, is_on=True, auto=True):
        super().__init__(is_on)
        self.auto = auto

    def turn_on(self):
        if self.is_on == True and self.auto == True:
            return "Лампа включена и установлен автоматический режим"
        else:
            return "лампа выключена"

light = Light(True)
smart_light = Smart_Light(True)
print(light.turn_on())
print(smart_light.turn_on())

#Задача 2
class Notification:

    def send(self, message: str):
        return f"Отправлено уведомление {message}"

class SMS_Notification(Notification):

    def send(self, message: str):
        return f"[SMS] {message}"

class Email_Notification(Notification):

    def send(self, message: str):
        return f"[Email] {message}"

sms = SMS_Notification()
email = Email_Notification()
print(sms.send("Привет"))
print(email.send("Привет"))

#Задача 3
class BaseSubscribtion:
    def __init__(self, price: int):
        self.price = price

    def get_features(self):
        return ["Просмотр в HD"]

class FamilySubscription(BaseSubscribtion):
    def __init__(self, price: int, max_devices: int):
        super().__init__(price)
        self.max_devices = max_devices

    def get_features(self):
        features = super().get_features()
        features.append("просмотр в 4К")
        return features

base = BaseSubscribtion(1000)
family = FamilySubscription(1000, 5)
print(base.get_features())
print(family.get_features())

#Задача 4
class Recipe:
    def __init__(self, name: str, cooking_time: int):
        self.name = name
        self.cooking_time = cooking_time

    def info(self):
        return f"Блюдо {self.name}, время {self.cooking_time} минут"

class Baking_recipe(Recipe):
    def __init__(self, name: str, cooking_time: int, oven_temperature: int):
        super().__init__(name, cooking_time)
        self.oven_temperature = oven_temperature

    def info(self):
        new_recipe = super().info()
        return f"{new_recipe}, температура в духовке {self.oven_temperature} градусов"

recipe = Recipe("Пицца", 120)
baking = Baking_recipe("Пицца", 120, 200)
print(recipe.info())
print(baking.info())

#Задача 5
class SpaceShip:
    def __init__(self, name: str, fuel: int):
        self.name = name
        self.fuel = fuel

    def fly(self):
        if self.fuel >= 10:
            self.fuel -= 10
            return f"Космический корабль {self.name} совершил перелет,в остатке {self.fuel} топлива"
        else:
            return "Нет топлива"

class BattleShip(SpaceShip):
    def __init__(self, name: str, fuel: int, ammo: int):
        super().__init__(name, fuel)
        self.ammo = ammo

    def shoot(self):
        if self.ammo > 0:
            return "Бабах! Успешный выстрел!"
        else:
            return "Обойма пуста"

    def fly(self):
        if self.fuel >= 20:
            self.fuel -= 20
            return f"Космический корабль {self.name} совершил перелет, в остатке {self.fuel} топлива"
        else:
            return "Нет топлива"

ship = SpaceShip("Обычный", 100)
battle = BattleShip("Боевой", 100, 5)
print(ship.fly())
print(battle.shoot())
print(battle.fly())

#Задача 6
class Delivery:
    def __init__(self, distance: int):
        self.distance = distance

    def calculate_cost(self):
        cost = self.distance * 5
        return f"Доставка обойдется в {cost} рублей"

    def get_delivery_days(self):
        delivery_days = self.distance // 100 + 1
        return f"Доставка займет {delivery_days} дней"

class ExpressDelivery(Delivery):
    def __init__(self, distance: int):
        super().__init__(distance)

    def calculate_cost(self):
        cost = self.distance * 12
        return f"Более дорогая доставка обойдется в {cost} рублей"

    def get_delivery_days(self):
        delivery_days = (self.distance // 100 + 1 // 2)
        return f"Доставка займет {delivery_days} дней"

delivery = Delivery(600)
express = ExpressDelivery(600)
print(delivery.calculate_cost())
print(delivery.get_delivery_days())
print(express.calculate_cost())
print(express.get_delivery_days())