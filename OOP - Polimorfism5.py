#Задача 1
class PaymentProccessor:
    def __init__(self, purchase: int, card_account: int, discount: float):
        self.purchase = purchase
        self.card_account = card_account
        self.discount = discount

    def processPayment(self, money_paid: int):
        if self.purchase <= self.card_account:
            self.purchase = money_paid
            money_paid *= self.discount
            self.card_account -= money_paid
            return f"Покупка успешно завершена, баланс на карте: {self.card_account} рублей"
        else:
            return f"Покупка не прошла, денег на карте нет!"

class PayPalProcessor:
    def __init__(self, phone_price: int, paypal_money_box: int, amount_of_buyers_money: int):
        self.phone_price = phone_price
        self.paypal_money_box = paypal_money_box
        self.amount_of_buyers_money = amount_of_buyers_money

    def processPayment(self, money_paid: int):
        if self.phone_price >= self.amount_of_buyers_money and money_paid <= self.amount_of_buyers_money:
            self.paypal_money_box += self.phone_price
            return f"Вы успешно продали свой телефон за {self.phone_price} рублей, на счету в PayPal у вас {self.paypal_money_box} рублей"
        else:
            return "Телефон не продан и покупка не удалась из-за недостатка денег у покупателя"

class CryptoProcessor:
    def __init__(self, internet: bool, product: str, product_price: int, bitcoin: int):
        self.internet = internet
        self.product = product
        self.product_price = product_price
        self.bitcoin = bitcoin

    def processPayment(self, money_paid: int):
        if self.internet == True and self.product_price >= money_paid and self.bitcoin > self.product_price:
            self.bitcoin -= self.product_price
            self.product_price /= self.bitcoin
            return f"Вы успешно купили за биткойн товар {self.product}, остаток на счету {self.product_price} биткоинов"
        else:
            return f"Нет биткоинов на счету"

def payment():
    payment_list = [PaymentProccessor(5000, 6000, 0.10), PayPalProcessor(50000, 0, 60000), CryptoProcessor(True, "Редкие часы Rolex", 1000000, 6800000)]

    for pay in payment_list:
        print(pay.processPayment(1000))

payment()

#Задача 2
class GameObject:
    def __init__(self, name: str, hp: int, weapon: str, weapon_damage: int, armor: bool, type: str):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.weapon_damage = weapon_damage
        self.armor = armor
        self.type = type

    def update(self):
        return f"Имя объекта - {self.name}, Хп - {self.hp}, Оружие - {self.weapon}, Урон данного оружия - {self.weapon_damage}, броня - {self.armor}, Тип объекта - {self.type}"

class Player(GameObject):
    def __init__(self, name: str,  hp: int, weapon: str, weapon_damage: int, armor: bool, type: str, direction_movement: str):
        super().__init__(name, hp, weapon, weapon_damage, armor, type)
        self.direction_movement = direction_movement

    def update(self, enemy1: str, hp1: int, damage: int):
        if self.direction_movement == "Прямо":
            self.hp -= damage
            print(f"враг-приспешник {enemy1} бьет вас, итого жизней {self.hp}")
            hp1 -= self.weapon_damage
            if self.armor == True or hp1 <= self.weapon_damage:
                return f"У игрока {self.name} Защита равна {self.armor}, урон противника не прошел, игрок убил противника"
            else:
                self.hp -= damage
                return f"враг-приспешник {enemy1} пережил удар игрока {self.name} и нанес ответный удар, количество жизней у игрока {self.name} - {self.hp}"
        elif self.direction_movement == "Налево":
            return f"На данном направлении игрок {self.name} не встретил никого, количество жизне равно {self.hp}, тип персонажа - {self.type}"

class Enemy(GameObject):
    def __init__(self, name: str, hp: int, weapon:str, weapon_damage: int, armor: bool, type: str, direction_movement: str, bot_direction_movement: str):
        super().__init__(name, hp, weapon, weapon_damage, armor, type)
        self.direction_movement = direction_movement
        self.bot_direction_movement = bot_direction_movement

    def update(self, new_name: str, hp2: int, damage2: int):
        if self.direction_movement == self.bot_direction_movement:
            print(f"Бот-враг {new_name}и игрок {self.name} пересеклись, враг игрока {self.name}, итого жизней {self.hp}")
            self.hp -= damage2
            if self.armor == True:
                return f"Игрок {self.name}, выстоял удар Бота-врага {new_name}"
            elif self.armor == False:
                hp2 -= self.weapon_damage
                return f"Игрок {self.name} наносит ответный удар, жизней у Бота-врага - {self.hp2}"
            else:
                self.hp -= damage2
                return f"Потрачено, игрок {self.name} погиб от Бота-Врага {new_name}"
        else:
            return f"Игрок{self.name} и бот {new_name} не пересеклись"


def fight():
    player = Player("Matvey", 100, "Меч", 50, True, "Рыцарь", "Прямо")
    enemy = Enemy("Бот-Враг", 80, "Топор", 30, False, "Орк", "Прямо", "Влево")

    print(player.update("Приспешник", enemy.hp, 20))
    print(player.update("Matvey", player.hp, 50))

fight()

#Задача 3
class DocumentExporter:
    def __init__(self, name: str, file_format: str, corrupted_file: bool):
        self.name = name
        self.file_format = file_format
        self.corrupted_file = corrupted_file

class PdfExporter(DocumentExporter):
    def __init__(self, name: str, file_format: str, corrupted_file: bool):
        super().__init__(name, file_format, corrupted_file)

    def save(self, saver: str):
        if self.file_format == saver and self.corrupted_file == False:
            return f"Файл {self.name} с форматом {self.file_format} успешно сохранен!"
        else:
            return f"Ошибка файл {self.name} не сохранен"

class CsvExporter(DocumentExporter):
    def __init__(self, name: str, file_format: str, corrupted_file: bool):
        super().__init__(name, file_format, corrupted_file)

    def save(self, saver: str):
        if self.file_format == saver and self.corrupted_file == False:
            return f"Файл {self.name} с форматом {self.file_format} успешно сохранен!"
        else:
            return f"Ошибка файл {self.name} не сохранен"

class JsonExporter(DocumentExporter):
    def __init__(self, name: str, file_format: str, corrupted_file: bool):
        super().__init__(name, file_format, corrupted_file)

    def save(self, saver: str):
        if self.file_format == saver and self.corrupted_file == False:
            return f"Файл {self.name} с форматом {self.file_format} успешно сохранен!"
        else:
            return f"Ощибка файл {self.name} не сохранен"

def export():
    exporter_list = [PdfExporter("Текст", "Pdf", False), CsvExporter("Таблица", "Csv", False), JsonExporter("Код", "Json", False)]

    for exporter in exporter_list:
        print(exporter.save("Pdf"))

export()

#