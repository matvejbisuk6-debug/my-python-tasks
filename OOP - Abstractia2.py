#Задача 1
from abc import ABC, abstractmethod

class Appliance(ABC):

    @abstractmethod
    def turn_on(self) -> None:
        pass

class WashingMachine(Appliance):

    def turn_on(self) -> str:
        return "Стиральная машина начинает цикл стирки"

class Refrigerator(Appliance):

    def turn_on(self) -> str:
        return "Холодильник включил компрессор для охдаждения"

washing_machine = WashingMachine()
refrigerator = Refrigerator()

print(washing_machine.turn_on())
print(refrigerator.turn_on())

#Задача 2
class AuthService(ABC):

    @abstractmethod
    def login(self, username: str, password: int) -> None:
        pass

class PasswordAuth(AuthService):

    def login(self, username: str, password: str) -> dict:
        if password == "1234":
            return True
        else:
            return False

class SmsCodeAuth(AuthService):

    def login(self, username: str, password: str) -> str:
        if len(password) == 4:
            return True
        else:
            return False

password_auth = PasswordAuth()
sms_auth = SmsCodeAuth()

print(password_auth.login("Matvey", "1234"))
print(sms_auth.login("Matvey", "1234"))

#Задача 3
class Invert_new(ABC):
    def __init__(self):
        self.dict = {"ice": "cold", "fire": "hot"}

    @abstractmethod
    def invert_dict(self, d) -> None:
        pass

class InvertDict(Invert_new):

    def invert_dict(self) -> str:
        return {value: key for key, value in self.dict.items()}

invert = InvertDict()

print(invert.invert_dict())

#Задача 4
class DataStorage(ABC):
    def __init__(self, file_name: str):
        self.file_name = file_name

    def connect(self):
        return f"Подключение к файлу {self.file_name} установлено"

    @abstractmethod
    def save_data(self, data) -> None:
        pass

class JsonStorage(DataStorage):
    def save_data(self, data) -> str:
        return f"Сохраняю данные в формате JSON: {data}"

class CsvStorage(DataStorage):
    def save_data(self, data) -> str:
        return f"Сохраняю данные в формате Csv: {data}"

json = JsonStorage("Сочи_2007")
csv = CsvStorage("Сочи_2007")

print(json.connect())
print(json.save_data("Какая-то информация"))
print(csv.connect())
print(csv.save_data("Какая-то информация"))

#Задача 5
class Spell(ABC):
    def __init__(self, mana_cost: int):
        self.mana_cost = mana_cost

    @abstractmethod
    def cast(self) -> str:
        pass

class ShieldSpell(Spell):

    def cast(self) -> str:
        return "Магический щит поглащает урон!"

class TeleportSpell(Spell):

    def cast(self) -> str:
        return "Персонаж мгновенно переместился вперед!"

shield = ShieldSpell(50)
teleport = TeleportSpell(100)

print(shield.cast())
print(teleport.cast())