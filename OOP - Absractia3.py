from abc import ABC, abstractmethod
from operator import truediv


#Задача 1
class PromoCode(ABC):
    def __init__(self, code: int):
        self.code = code

    @abstractmethod
    def is_valid(self, cart_total: float) -> float:
        pass

    @abstractmethod
    def apply(self, cart_total: float) -> float:
        pass

class FirstOrderPromo(PromoCode):
    def __init__(self, code: str):
        super().__init__(code)

    def is_valid(self, cart_total: int) -> str:
        if cart_total > 1000 and self.code == "12345":
            return f"{cart_total} - Действителен всегда"
        else:
            return  f"{cart_total} - Не действителен"

    def apply(self, cart_total: int) -> str:
        cart_total -= 300
        return f"Итоговая стоимомть корзины - {cart_total} рублей"

class WholesalePromo(PromoCode):
    def __init__(self, code: str):
        super().__init__(code)

    def is_valid(self, cart_total: int) -> str:
        if cart_total >= 1000 and self.code == "12345":
            return f"{cart_total} - Действителен всегда"
        else:
            return f"{cart_total} - Не действителен"

    def apply(self, cart_total: float) -> str:
        cart_total -= cart_total * 0.15
        return f"Итоговая стоимомть корзины - {cart_total} рублей"

first = FirstOrderPromo("12345")
whole = WholesalePromo("12345")

print(first.is_valid(1001))
print(first.apply(1001))
print(whole.is_valid(10000))
print(whole.apply(10000))

#Задача 2
class InputController(ABC):

    @abstractmethod
    def move_forward(self) -> str:
        pass

    @abstractmethod
    def move_backward(self) -> str:
        pass

    @abstractmethod
    def jump(self) -> str:
        pass

    @abstractmethod
    def attack(self) -> str:
        pass

class KeyboardController(InputController):

    def move_forward(self) -> str:
        return "Нажата клавиша w: персонаж идет вперед"

    def move_backward(self) -> str:
        return "Нажата клавиша s: персонаж идет назад"

    def jump(self) -> str:
        return "Нажата клавиша пробел: персонаж прыгнул"

    def attack(self) -> str:
        return "нажата клавиша х: персонаж атакует"

class GameEngine:
    def __init__(self, controller):
        self.controller = controller
        self.is_running = True

    def game_loop(self):
        """Основной игровой цикл, последовательно вызывающий  4 действия"""
        while self.is_running:
            print(self.controller.move_forward())
            print(self.controller.move_backward())
            print(self.controller.jump())
            print(self.controller.attack())

            self.is_running = False

my_controller = KeyboardController()
engine = GameEngine(my_controller)
engine.game_loop()

#Задача 3
class DataExport(ABC):

    @abstractmethod
    def export(self, data_list: list) -> str:
        pass

class HTMLExport(DataExport):

    def export(self, data_list: list) -> str:
        data_list = ["Иван", "Анна"]
        html_items = [f"<li>{item}</li>" for item in data_list]
        return "".join(html_items)

class TextExport(DataExport):

    def export(self, data_list: list) -> str:
        data_list = ["Иван", "Анна"]
        line = [f"{i}" for i in data_list]
        return ", ".join(line)

data_list = ["Иван", "Анна"]

html = HTMLExport()
text = TextExport()

print(html.export(data_list))
print(text.export(data_list))

#Задача 4
class Transaction(ABC):
    def __init__(self, amount: int):
        self.amount = amount
    @abstractmethod
    def process(self, account: bool) -> str:
       pass

class PaymentTransaction(Transaction):
    def __init__(self, amount: int, balance: int):
        super().__init__(amount)
        self.balance = balance

    def process(self, amount: bool) -> str:
        if self.balance >= self.amount:
            self.balance -= self.amount
            print(f"Итоговый баланс равен {self.balance} рублей")
            return True
        else:
            return False

class CashbackTransaction(Transaction):
    def __init__(self, amount: int, balance: int):
        super().__init__(amount)
        self.balance = balance

    def process(self, account: bool) -> str:
        self.balance += self.amount
        print(self.balance)
        return True

account = True

payment = PaymentTransaction(5000, 10000)
cashback = CashbackTransaction(5000, 10000)

print(payment.process(account))
print(cashback.process(account))