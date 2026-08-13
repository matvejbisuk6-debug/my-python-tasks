#Задача 1
class Button:
    def __init__(self, secret_code: int):
        self.__secret_code = secret_code

    def show_code(self):
        return self.__secret_code

button = Button(42)
print(button.show_code())

#Задача 2
class PiggyBank:
    def __init__(self, coins: int):
        self.__coins = coins

    def add_coins(self, amount: int):
        if self.__coins > 0:
            self.__coins += amount
        else:
            return "Нельзя добавить деньги"

    def see_bank(self):
        return f"Текущий баланс равен {self.__coins} рублей"

bank = PiggyBank(140)
bank.add_coins(10)
print(bank.see_bank())

#Задача 3
class Car:
    def __init__(self, speed: int):
        self.__speed = speed

    @property
    def speed(self):
        return f"Текущая скорость равна {self.__speed}"

    @speed.setter
    def speed(self, amount: int):
        if amount > 200 or amount < 0:
            print("Неверная скорость!Допустимо от 0 до 200 км/ч ")
        else:
            self.__speed = amount

speed = Car(140)
speed.speed = 139
print(speed.speed)

#Задача 4
class User:
    def __init__(self, password: int):
        self.__password = password

    def check_password(self, enter):
        if self.__password == enter:
            return True
        else:
            return False

user = User("672344")
print(user.check_password("682344"))