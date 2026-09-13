#Задача 1
from abc import ABC, abstractmethod

class Venicle(ABC):

    @abstractmethod
    def start_engine(self) -> None :
        pass

class Car(Venicle):

    def start_engine(self) -> str:
        return "Машина: Двигатель заведен, вжжууух!"

class Motorcycle(Venicle):

    def start_engine(self) -> str:
        return "Мотоцикл: рев мотора, рррр!"

my_car = Car()
my_bike = Motorcycle()

print(my_car.start_engine())
print(my_bike.start_engine())