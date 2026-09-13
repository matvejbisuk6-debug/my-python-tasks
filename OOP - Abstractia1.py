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

#Задача 2
class Instrument(ABC):

    @abstractmethod
    def play_sound(self) -> None:
        pass

class Guitar(Instrument):

    def play_sound(self) -> str:
        return "Брынь-брынь!"

class Drum(Instrument):

    def play_sound(self) -> str:
        return "Бум-бам!"

class Piano(Instrument):

    def play_sound(self) -> str:
        return "Ля-ля-ля"

guitar = Guitar()
drum = Drum()
piano = Piano()

print(guitar.play_sound())
print(drum.play_sound())
print(piano.play_sound())
