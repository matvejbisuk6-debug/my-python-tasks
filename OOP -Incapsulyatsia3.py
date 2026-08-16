#Задача 1
class Autentification:
    def __init__(self, name: str, password: int, token: int):
        self.name = name
        self.__password = password
        self.__token = token

    def login(self):
        return "Телеграмм успешно работает!"

    def change_password(self, old: int, new: int, new_token: int):
        if self.__password == new and self.__token:
            self.__password = new
            return f"{self.name} получил доступ к телеграмм боту"
        else:
            return f"{self.name} Доступ к телеграмм боту запрещен"

tg_bot = Autentification("Matvey", 171828, 373632828)
tg_bot.change_password(171828, 728272, 727727299)
print(tg_bot.login())

#Задача 2
class Bank:
    def __init__(self, balance: int, percent_stavka: float, pin: str):
        self.__balance = balance
        self.history = [balance]
        self.percent_stavka = percent_stavka
        self.__pin = pin
        self.credit = 0

    @property
    def withdraw(self):
        return f"История Транзакций - {self.history}, кредит равен - {self.credit}"

    def get_history(self, entered_pin: str):
        if self.__pin == entered_pin:
            return f"История транзакций: {self.history}"
        else:
            return "Неправильны ПИН-код!"

    def deposit(self, amount):
        if self.__balance > 0:
            self.credit = amount + (amount * self.percent_stavka)
            self.__balance += amount
            self.history.append(amount)
            print(f"Кредит взят, чеез пол года вам нужно отдать {self.credit} рублей")
        else:
            print("Кредит невозможен потому что нет денег на балансе")

moneys_bank = Bank(10000, 0.15, "1234")
moneys_bank.deposit(40000)
print(moneys_bank.get_history("1234"))
print(moneys_bank.withdraw)

#Задача 3
class Game:
    def __init__(self, hp: int, based_damage: int, coordination: str, defender: bool, coordinates_of_enemy:str):
        self.__hp = hp
        self.based_damage = based_damage
        self.__coordination = coordination
        self.__defender = defender
        self.coordination_of_enemy = coordinates_of_enemy

    @property
    def player(self):
        return f"Игрок жив и наносит удар по координатамм врага {self.coordination_of_enemy}"

    def heal(self):
        if self.__hp > 0 and self.__hp <= 100:
            print(f"Игрок возвращает урон на координаты {self.coordination_of_enemy}")

    def take_damage(self, amount: int):
        if self.__defender == True:
            amount -= 10
            if self.__hp > 0:
                self.__hp -= amount
                print("Игрок живой продолжает битву")
            else:
                print("Игрок мертв")

rpg_game = Game(100, 5, "27.18181.111", True, "91.18291.129")
rpg_game.take_damage(20)
print(rpg_game.player)

#Задача 4
class Api:
    def __init__(self, secret_api_key: int, connection_status: bool, weather_in_Pereslavl: int):
        self.__secret_api_key = secret_api_key
        self.__connection_status = connection_status
        self.weather_in_Pereslavl = weather_in_Pereslavl

    @property
    def send_data(self):
        return f"Температура на метостанции в Переславле-Залесском изменена и равна {self.weather_in_Pereslavl} градусов"

    def connect(self, new_temperature: int, enter_api: int):
        if enter_api == self.__secret_api_key and self.__connection_status == True:
            self.weather_in_Pereslavl = new_temperature
            print(f"Темература равна {self.weather_in_Pereslavl} градусов")
        else:
            print("API ключ введен некорректно, либо статус подключения уровня false")

weather_api = Api(18181818, True, +18)
weather_api.connect(+19, 18181818)
print(weather_api.send_data)

#Задача 5
class Climate:
    def __init__(self, temperature: int, fan_speed: int, password: int):
        self.__temperature = temperature
        self.fan_speed = fan_speed
        self.__password = password

    @property
    def temperature(self):
        return f"Новый климат контроль равен температуре {self.__temperature} градусов, бороты вентилятора {self.fan_speed}"

    def climate_controle(self, enter_password: int, new_temperature: int, new_fan_speed: int):
        if enter_password == self.__password:
            self.__temperature = new_temperature
            self.fan_speed = new_fan_speed
            print(f"Текущий климат контроль в комнате: Температура {self.__temperature} градусов, скорость вентилятора: {self.fan_speed}")
        else:
            print(f"Неправильный пароль, климат контроль не отображается")

climate_room = Climate(30, 1, 127171)
climate_room.climate_controle(127171, +22, 4)
print(climate_room.temperature)