#Задача 1
from abc import ABC, abstractmethod

class Appliance(ABC):

    @abstractmethod
    def turn_on(self) -> None:
        pass

class WashingMachine(Appliance):

    def turn_on(self) -> str:
        return "Стиральная машина начинает цикл стирки"

class Refrigerator(Appliance):

    def turn_on(self) -> str:
        return "Холодильник включил компрессор для охдаждения"

washing_machine = WashingMachine()
refrigerator = Refrigerator()

print(washing_machine.turn_on())
print(refrigerator.turn_on())