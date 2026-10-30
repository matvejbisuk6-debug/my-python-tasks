import functools
import time

#Задача 1
correct_pin = "4815"
attempts = 0

while True:
    enter_pin = str(input("Введите Пин-код: "))
    attempts += 1
    if enter_pin == correct_pin:
        print("Пароль верен, доступ разрешен!")
        break
    elif attempts >= 3:
        print("Сейф заблокирован, попытки закончились.")
        break
    else:
        print(f"Неправильно, осталось попыток: {attempts}")

#Задача 2
def cache_result(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper


@cache_result
def heavy_calculation(x):
    x *= 2
    time.sleep(2)
    return x

print(heavy_calculation(3))
print(heavy_calculation(3))

#Задача 3
class Bank_card:
    def __init__(self, card_holder: str, balance: int):
        self.card_holder = card_holder
        self.balance = balance

    def top_up(self, amount):
        self.balance += amount
        return f"Ваш баланс у пользователя {self.card_holder} пополнен и равен {self.balance} рублей"

    def pay(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Покупка оформлена, баланс карты пользователя {self.card_holder} равен {self.balance} рублей"
        else:
            return f"Недостаточно средств на карте у пользователя {self.card_holder}"

    def get_balance(self):
        return f"Текущий остаток на карте пользователя {self.card_holder} равна {self.balance} ублей"

bank_card = Bank_card("Матвей", 1000)
print(bank_card.top_up(1000))
print(bank_card.pay(999))
print(bank_card.get_balance())