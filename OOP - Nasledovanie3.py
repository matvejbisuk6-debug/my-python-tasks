#Задача 1
class Item:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    def use(self):
        return f"Вы исользовали {self.name} которое весит {self.weight} кг"

class Weapon(Item):
    def __init__(self, name: str, weight: int, damage: int):
        super().__init__(name, weight)
        self.damage = damage

    def use(self):
        new_info = super().use()
        return f"{new_info} и нанесли {self.damage} урона"

item = Item("Меч", 4)
weapon = Weapon("Меч", 4, 10)
print(weapon.use())

#Задача 2
class Sensor:
    def __init__(self, location: str):
        self.location = location

    def get_status(self):
        return f"датчик в комнате {self.location} работает"

class TemperatureSensor(Sensor):

    def get_status(self):
        temperature = super().get_status()
        return f"{temperature} и фиксирует 22 градуса"

class SmokeSensor(Sensor):

    def get_status(self):
        smoke_sensor = super().get_status()
        return f"{smoke_sensor}, дым не зафиксирован"

sensor = Sensor("Кухня")
temp_sensor = TemperatureSensor("Спальня")
smoke = SmokeSensor("Зал")
print(sensor.get_status())
print(temp_sensor.get_status())
print(smoke.get_status())