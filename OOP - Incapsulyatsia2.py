#Задача 1
class Safe:
    def __init__(self, password: int):
        self.__password = password
        self.__money = 0

    def add_money (self, amount: int):
        self.__money += amount

    def get_money(self, entered_password: int):
        if self.__password == entered_password:
            return self.__money
        else:
            return "Доступ запрещен"

money_safe = Safe(111307)
money_safe.add_money(250)
print(money_safe.get_money(111307))

#Задача 2
class UserProfile:
    def __init__(self, user_name: str, password: int):
        self.__password = password
        self.user_name = user_name

    def update_password(self, old_password: int, new_password: int):
        if self.__password == old_password:
            self.__password = new_password
            return "Новый пароль установлен"
        else:
            return "Ошибка: старый пароль указан неверно!"

user = UserProfile("Matvey", 121234)
print(user.update_password(133567,588558))

#Задача 3
class Thermometer:
    def __init__(self, celsius: int):
        self.__celsius = celsius

    def get_temperature(self):
        return self.__celsius

    def set_temperature(self, value: int):
        if value > 273.15 and value < 1000:
            self.__celsius = value
        else:
            return "Предупреждение!Введено некоректное значение!"

temperature = Thermometer(0)
temperature.set_temperature(-25)
print(temperature.get_temperature())

#Задача 4
class BankCard:
    def __init__(self, holder: str, balance: int):
        self.holder = holder
        self.__balance = balance
        self.__pin = "1234"

    def show_balance(self, entered_pin: str):
        if self.__pin == entered_pin:
            return self.__balance
        else:
            return "Неправильный ПИН-код"

    def change_pin(self, old_pin: str, new_pin: str):
        if old_pin == self.__pin and type(new_pin) == str:
            self.__pin = new_pin

card = BankCard("Matvey", 10000)
card.show_balance("1234")
card.change_pin("1234", "7777")
print(card.show_balance("7777"))

#Задача 5
class Open_app:
    def __init__(self, battery_level: int):
        self.__battery_level = battery_level
        self.__is_on = False

    def turn_on(self):
        if self.__battery_level > 0:
            self.__is_on = False

    def open_app(self, app_name: str):
        if self.__is_on == True:
            self.__battery_level -= 10
            return f"Открываю {app_name}"
        if self.__battery_level == 0:
            self.__is_on = False
            return f"Открывая {app_name}, но телефон выклюячился"

    def charge(self, amount: int):
        self.__battery_level += amount
        if self.__battery_level >= 100:
            self.__battery_level = 100
            return "Телефон полностью заряжен"

app = Open_app(100)
app.turn_on()
app.charge(1)
print(app.open_app("Youtube"))