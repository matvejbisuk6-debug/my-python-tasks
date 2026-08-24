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

#Задача 3
class BaseAccount:
    def __init__(self, balance: int):
        self.balance = balance

    def wihdraw(self, amount):
        if self.daysleft > amount:
            self.daysleft -= amount
            return True
        else:
            return False
class SavingAccount(BaseAccount):
    def __init__(self, balance: int, min_balance: int):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.min_balance < self.balance:
            self.balance -= amount
            return True
        else:
            return False

base = BaseAccount(1000)
saving = SavingAccount(1000, 200)
print(base.wihdraw())
print(saving.wihdraw())

#Задача 4
class Ticket:
    def __init__(self, seat_number: int, base_price: int):
        self.seat_number = seat_number
        self.base_price = base_price

    def get_price(self):
        return self.base_price

class VipTicket(Ticket):
    def __init__(self, seat_number, base_price: int, has_lounge_access: bool):
        super().__init__(seat_number, base_price)
        self.has_lounge_access = has_lounge_access

    def get_price(self):
        self.base_price *= 1.5
        return self.base_price

    def get_perks(self):
        if self.has_lounge_access == True:
            return ["Проход без очереди", "Доступ в Лаундж"]
        else:
            return ["Проход без очереди"]

ticket = Ticket(5, 200)
vip = VipTicket(5, 200, True)
print(ticket.get_price())
print(vip.get_price())
print(vip.get_perks())

#Задача 5
class Printer:
    def __init__(self, ink_level: int):
        self.ink_level = ink_level

    def print_page(self, text: str):
        if self.ink_level >= 5:
            self.ink_level -= 5
            return f"{text}. Осталось {self.ink_level} чернил"
        else:
            return "Нет чернил"

class ColorPrinter(Printer):
    def __init__(self, ink_level: int, color_ink_level: int):
        super().__init__(ink_level)
        self.color_ink_level = color_ink_level

    def print_page(self, text: str):
        if self.ink_level >= 2 and self.color_ink_level >= 7:
            self.ink_level -= 2
            self.color_ink_level -= 7
            return f"Осталось {self.ink_level} черных чернил и {self.color_ink_level} цветных чернил"
        else:
            return "Нет чернил"

printer = Printer(100)
color = ColorPrinter(100, 100)
print(printer.print_page("Привет, как дела?"))
print(color.print_page("Привет, как дела?"))

#Задача 6
class Subscription:
    def __init__(self, username: str, daysleft: int):
        self.username = username
        self.daysleft = daysleft

    def access_content(self):
        if self.daysleft > 0:
            self.daysleft -= 1
            return True
        else:
            return False

class AutoRenewSubscription(Subscription):
    def __init__(self, username: str, daysleft: int, card_balance: int, renew_cost: int):
        super().__init__(username, daysleft)
        self.card_balance = card_balance
        self.renew_cost = renew_cost

    def access_content(self):
        if self.daysleft > 0:
            return super().access_content()
        elif self.daysleft == 0:
            if self.card_balance >= self.renew_cost:
                self.card_balance -= self.renew_cost
                self.daysleft += 30
                return True
            else:
                return False

subscription = Subscription("Matvey", 30)
auto_renew = AutoRenewSubscription("Matvey", 30, 1000, 300)
print(subscription.access_content())
print(auto_renew.access_content())