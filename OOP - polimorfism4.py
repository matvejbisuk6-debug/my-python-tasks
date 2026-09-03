#Задача 1
class SmsNotification:
    def __init__(self, number_phone: int):
        self.number_phone = number_phone

    def send(self, message: str):
        return f"Отправлено SMS на номер {self.number_phone}: {message}"

class TelegramNotification:
    def __init__(self, chat_id: int):
        self.chat_id = chat_id

    def send(self, message: str):
        return f"Отправлено сообщение в Телеграм чат - {self.chat_id}: {message}"

class EmailNotification:
    def __init__(self, email: str):
        self.email = email

    def send(self, message: str):
        if len(self.email) > 100:
            new_message = message[:100]
            return f"Отправлено Email на {self.email}: {new_message}"
        else:
            return f"Отправлено Email на {self.email}: {message}"

class NotificationRouter:
    def broadcast(self):
        notifiction_list = [SmsNotification(79991234567), TelegramNotification(12345678), EmailNotification("test@example.com")]

        test_message = "Привет! Это очень важное уведомление для всех пользователей системы."
        for notificator in notifiction_list:
            print(notificator.send(test_message))

notification = NotificationRouter()
notification.broadcast()

#Задача 2
class Weapon:
    def __init__(self, name: str, weight: int, damage: int):
        self.name = name
        self.weight = weight
        self.damage = damage

    def get_stats(self):
        return {"weight": self.weight, "power": self.damage}

class Armor:
    def __init__(self, name: str, weight: int, defence: int):
        self.name = name
        self.weight = weight
        self.defence = defence

    def get_stats(self):
        return {"weight": self.weight, "power": self.defence}

class Potion:
    def __init__(self, name: str, volume: int):
        self.name = name
        self.volume = volume

    def get_stats(self):
        return {"weight": self.volume, "power": 0}

class Inventory:
    def calculate_total_weight(self):
        items_list = [Weapon("Меч", 10, 5), Armor("Щит", 10, 5), Potion("Молния", 5)]

        total_weight = 0

        for item in items_list:
            stats = item.get_stats()
            print(stats)

            total_weight += stats["weight"]

        print(f"Общий вес всех предметов: {total_weight}")


inventory = Inventory()
inventory.calculate_total_weight()

#Задача 3
class Profanity:
    def __init__(self):
        self.list = ["плохо", "глупо"]

    def clean(self, comment: str):
        for word in self.list:
            comment = comment.replace(word, "*****")
            return comment

class LinkFilter:
    def clean(self, comment: str):
        if comment.startswith("https://") :
            return f"Ссылка {comment} удалена"
        else:
            return comment

class SpacesFilter:
    def clean(self, comment: str):
        new_string = comment.strip().split()
        return " ".join(new_string)

class Moderator:
    def procces_comment(self, text: str):
        filter_list = [Profanity(), LinkFilter(), SpacesFilter()]

        for filter in filter_list:
            text = filter.clean(text)
            print(text)

moderator = Moderator()
moderator.procces_comment("  Это  плохо  ")

#Задача 4
class FullTimeEmployee:
    def __init__(self, monthly_salary: int):
        self.monthly_salary = monthly_salary

    def calculate_pay(self):
        return self.monthly_salary

class HourlyEmployee:
    def __init__(self, hourly_rate: int, hours_workers):
        self.hourly_rate = hourly_rate
        self.hours_workers = hours_workers

    def calculate_pay(self):
        self.hourly_rate *= self.hours_workers
        return f"Зарплата в почасовуой ставке - {self.hourly_rate} рублей"

class ComissionEmployee:
    def __init__(self, based_salary: int, sales_volume: int, comission_rate: float):
        self.based_salary = based_salary
        self.sales_volume = sales_volume
        self.comission_rate = comission_rate

    def calculate_pay(self):
        self.new_salary = self.based_salary + (self.sales_volume * self.comission_rate)
        return f"Зарплата меенеджера по продажам {self.new_salary} рублей"

def employee():
    employee_list = [FullTimeEmployee(60000), HourlyEmployee(500, 160), ComissionEmployee(30000, 200000, 0.1)]

    for emp in employee_list:
        print(emp.calculate_pay())

employee()

#Задача 5
class Player:
    def __init__(self, name: str, has_key: bool, intellect: int):
        self.name = name
        self.has_key = has_key
        self.intellect = intellect

class Chest:
    def interact(self, player: Player):
        if player.has_key == True:
            return "Сундук открыт! Вы нашли золото."
        else:
            return "Сундук заперт, нужен ключ"

class AncientBook:
    def interact(self, player: Player):
        if player.intellect >= 15:
            return "Вы постигли тайные знания!"
        else:
            return "Текст кажется вам набором непонятных символов."

class Pedestal:
    def interact(self, player: Player):
        if player.has_key == True:
            return "Вы нажали на рычаг. Из стены выпал ключ!"
        else:
            return "Не удалось нажать на рычаг"

def object():
    hero = Player("Матвей", True, 19)
    objects_list = [Chest(), AncientBook(), Pedestal()]

    for object in objects_list:
        print(object.interact(hero))

object()
