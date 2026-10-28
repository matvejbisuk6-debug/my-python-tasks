import functools
import asyncio

#Задача 1
def process_orders(orders, VIP_order):
    order1 = {"id": 121233, "client": "VIP_orders", "items": [{"price": 10000}]}
    order2 = {"id": 232324, "client": "orders", "items": [{"price":5000.0}]}

    for order in [order1, order2]:
        print(f"Обработка заказа {order1["id"]}")
        if order["client"] == "VIP_orders":
            price1 = order1["items"][0]["price"]
            new_price1 = price1 * 0.15
            print(f"Скидка составила у VIP-заказчика {VIP_order}составила {new_price1} рублей")
        elif order["client"] == "orders":
            price2 = order2["items"][0]["price"]
            if price2 > 10000:
                new_price2 = price2 * 0.05
                print(f"Скидка у заказчика {orders} составила {new_price2} рублей")
            elif price2 > 20000:
                new_price3 = price2 * 0.10
                print(f"Скидка у заказчика {orders} составила {new_price3} рублей")

print(process_orders("Матвей", "Леон"))

#Задача 2
def retry(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@retry
def retries(retries, exceptions):

    for i in exceptions:
        if i not in exceptions:
            return exceptions
        print(f"Ошибка {exceptions}. Осталось попыток {retries}")
        if TypeError and ValueError in exceptions:
            retries += 1
            print(f"Ошибка {exceptions}. Осталось попыток {retries}")

print(retries(0, (ValueError, TypeError)))

#Задача 3
class SmartDevice:
    def __init__(self, name: str, is_on: bool):
        self.name = name
        self.is_on = is_on

    def turn_on(self):
        return "Смарт-дом включен"

    def turn_off(self):
        return "Смарт-дом выключен"

class DimmableLight(SmartDevice):
    def __init__(self, name: str, is_on: bool, brightness: int):
        super().__init__(name, is_on)
        self.__brightness = brightness

    def get_light(self):
        return self.__brightness

    @property
    def light(self):
        if self.__brightness < 100 or self.__brightness > 0 and self.is_on == True:
            return f"Уровень яркости в комнате равен {self.__brightness} % при помощи умного дома {self.name}"
        else:
            return f"Уровень яркости настроен некорректно, умный дом {self.name}ошибка - ValueError"

class SmartHome(SmartDevice):
    def __init__(self, name: str, is_on: bool):
        super().__init__(name, is_on)
        self.devices = ["Голосовой помощник", "Датчик", "Пульт"]

    def add_device(self):
        for i in self.devices:
            quantity = len(self.devices)
            return f"Устройства для умного дома {self.name}- {i}, их количество равно {quantity}, Он включен - {self.is_on}"

dimmablelight = DimmableLight("Яндекс Алиса", True, 77)
smarthome = SmartHome("Яндекс Алиса", True)
print(dimmablelight.get_light())
print(smarthome.add_device())

#Задача 4
async def fetch_errors(file_name, delay):
    print(f"Читаю файл - {file_name}")
    await asyncio.sleep(delay)
    return [f"Error 404 в {file_name}", f"Error 500 в {file_name}."]

async def main():
    results = await asyncio.gather(
        fetch_errors("Курсач 2027", 1),
        fetch_errors("Отчет ПП", 2),
        fetch_errors("Диплом 2027", 3)
    )
    print(f"Все результаты получены: ", results)

asyncio.run(main())
