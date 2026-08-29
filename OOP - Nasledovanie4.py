#Задача 1
from types import new_class


class Character:
    def __init__(self, name: str, health: int, damage: int):
        self.name = name
        self.health = health
        self.damage = damage
        self.troll_killed = []

    def take_damage(self, troll_health: int, troll_damage: int, text: str):
        if troll_damage <= self.damage:
            self.troll_killed.append(text)
            return "Тролль 1 убит"
        elif troll_health > self.damage:
            self.health -= troll_damage
            return f"Тролль 1 наносит ответный удар у игрока {self.name} - {self.health} hp"
        else:
            self.troll_killed.append(text)
            return "Тролль 1 мертв"

class Mage(Character):
    def __init__(self, name: str, health: int, damage: int, mage: int):
        super().__init__(name, health, damage)
        self.mage = mage

    def take_damage(self, troll_health: int, troll_damage: int, text: str):
        new_damage = self.damage + self.mage
        if troll_damage <= new_damage:
            self.troll_killed.append(text)
            return "Тролль 2 убит"
        elif troll_health > new_damage:
            self.health -= troll_damage
            return f"Тролль 2 наносит ответный удар у игрока {self.name} - {self.health} hp"
        else:
            self.troll_killed.append(text)
            return "Тролль 2 мертв"

    def take_damage_boss(self, boss_health: int, boss_damage: int, text: str):
        new_damage = self.damage + self.mage
        if boss_health <= new_damage:
            self.troll_killed.append(text)
            return f"Босс убит, {self.troll_killed}"
        elif boss_health > self.damage:
            self.health -= boss_damage
            return f"Босс наносит ответный удар у игрока {self.name} - {self.health} hp"
        else:
            self.troll_killed.append(text)
            return f"Босс мертв, {self.troll_killed}"

character = Character("Matvey", 100, 5)
boss = Mage("Matvey", 100, 5, 20)
print(character.take_damage(5, 2, "Тролль1 убит"))
print(boss.take_damage(15, 5, "Тролль2 приспешник убит"))
print(boss.take_damage_boss(25, 25, "Король Троллей убит"))

#Задача 2
class User:
    def __init__(self, name: str, year_old: int):
        self.name = name
        self.year_old = year_old

class Base_Command(User):
    def __init__(self, name: str, year_old: int, command_start: bool):
        super().__init__(name, year_old)
        self.command_start = command_start

    def execute(self):
        if self.command_start == True and self.year_old >= 18:
            return f"Поздравляем! {self.name} Телеграмм бот запущен!"
        else:
            return "Error"

class SettingsCommand(User):
    def __init__(self, name: str, year_old: int, command_settings: str):
        super().__init__(name, year_old)
        self.command_settings = command_settings

    def execute(self):
        return f"Команда /settings включена, язык - {self.command_settings}"

class HelpCommand(User):
    def __init__(self, name: str, year_old: int, help_command: bool):
        super().__init__(name, year_old)
        self.help_command = help_command

    def execute(self, text: str):
        if self.help_command == True and self.year_old >= 18:
            return f"Поздравляем, {self.name}! Завтра мы поможем вам {text}"
        else:
            return "Мы не поможем вам."

base = Base_Command("Matvey", 19, True)
setting = SettingsCommand("Matvey", 19, "Немецкий")
help = HelpCommand("Matvey", 19, True)
print(base.execute())
print(setting.execute())
print(help.execute("помириться с другом"))

#Задача 3
class Employee:
    def __init__(self, name: str, based_rate: int, bonus: float):
        self.name = name
        self.based_rate = based_rate
        self.bonus = bonus

class Developer(Employee):
    def __init__(self, name: str, based_rate: int, bonus: int, tg_bot_freelance: int):
        super().__init__(name, based_rate, bonus)
        self.tg_bot_freelance = tg_bot_freelance

    def calculate_salary(self):
        if self.based_rate > 0:
            salary = self.based_rate + self.tg_bot_freelance + self.bonus
            return f"Итоговый оклад разработчика {self.name} - {salary} рублей"
        else:
            return "Error, вы не работали"

class Freelance(Employee):
    def __init__(self, name: str, based_rate: int, bonus: int, hours: int):
        super().__init__(name, based_rate, bonus)
        self.hours = hours

    def calculate_salary(self):
        if self.based_rate > 0:
            salary = (self.based_rate + self.bonus) + (self.hours * self.based_rate)
            return f"Итоговый оклад фрилансера {self.name} - {salary} рублей"
        else:
            return "Error"

developer = Developer("Matvey", 50000, 10000, 5000)
freelance = Freelance("Alqxey", 200, 5000, 160)
print(developer.calculate_salary())
print(freelance.calculate_salary())

#Задача 4
class Parser:
    def __init__(self, name: str, price_salary: int, internet: bool, errors: bool):
        self.name = name
        self.price_salary = price_salary
        self.internet = internet
        self.errors = errors
        self.parser = {}

class AvitoParser(Parser):
    def __init__(self, name: str, price_salary: int, internet: bool, errors: bool, city: str, discount: float):
        super().__init__(name, price_salary, internet, errors)
        self.city = city
        self.discount = discount

    def api_parser(self):
        if self.internet == True and self.errors == False:
            new_price = self.price_salary - (self.price_salary * self.discount)
            self.parser[self.name] = new_price
            return f"Товар {self.name} без скидки стоит {self.price_salary} рублей, а со скидкой {new_price} рублей, местоположение - нп. {self.city}"
        else:
            return "товар не добавлен, error"

class HabrParser(Parser):
    def __init__(self, name: str, price_salary: int, internet: bool, errors: bool, city: str, bonus: int):
        super().__init__(name, price_salary, internet, errors)
        self.city = city
        self.bonus = bonus

    def api_parcer(self):
        if self.internet == True and self.errors == False:
            new_price = self.price_salary + self.bonus
            self.parser[self.name] = new_price
            print(self.parser)
            return f"Бэкэндер {self.name} получил оффер на работу в нп. {self.city} и будет получать {new_price} рублей в месяц"
        else:
            return "Error"

avito = AvitoParser("Lenovo Legion", 40000, True, False, "Переславль-Залесский", 0.20)
habr = HabrParser("Матвей", 80000, True, False, "Москва", 20000)
print(avito.api_parser())
print(habr.api_parcer())

#Задача 5
class BankAccount:
    def __init__(self, balance: int, pin: int):
        self.balance = balance
        self.pin = pin

class SavingAccount(BankAccount):
    def __init__(self, balance: int, pin: int, percent: float, credit:bool):
        super().__init__(balance, pin)
        self.percent = percent
        self.credit = credit

    def take_credit(self, enter_pin: int, money_credit: int):
        if self.balance > 0 and enter_pin == self.pin and self.credit == True:
            new_balance = money_credit + self.balance
            return f"Вы оформили кредит под {self.percent} процентов на сумму {money_credit}, теерь ваш баланс равен {new_balance} рублей"
        else:
            return "Кредит не оформлен, error"

class CreditAccount(BankAccount):
    def __init__(self, balance: int, pin: int, credit: bool, salary: int, percent: float):
        super().__init__(balance, pin)
        self.credit = credit
        self.salary = salary
        self.percent = percent

    def take_credit(self, enter_pin: int, money_credit: int):
        if self.balance > 0 and enter_pin == self.pin and self.credit == True:
            new_salary = self.salary - (self.salary * self.percent)
            new_balance = self.balance - (self.salary - self.percent)
            return f"Вы выплатили кредит в {money_credit} рублей - итоговая арплата равна {new_salary} рублей, а баланс равен {new_balance} рублей"
        else:
            return "За вами придут коллекторы, вы ничего не выполнили"

save = SavingAccount(50000, 1000, 1000, 1234)
credit = CreditAccount(50000, 1000, 1000, 0.15, 1234)
print(save.take_credit(1234, 20000))
print(credit.take_credit(1234, 20000))