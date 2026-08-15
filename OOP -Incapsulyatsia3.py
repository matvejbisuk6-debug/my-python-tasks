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