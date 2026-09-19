from abc import ABC, abstractmethod

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