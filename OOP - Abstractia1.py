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

#Задача 3
class Employee(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_salary(self) -> None:
        pass

class FulltimeEmployee(Employee):
    def __init__(self, name: str, monthly_pay: int):
        super().__init__(name)
        self.monthly_pay = monthly_pay

    def get_salary(self) -> str:
        return f"Ежемесячная зарплата гражданина {self.name} равна {self.monthly_pay}"

class Freelancer(Employee):
    def __init__(self, name: str, hourly_rate: int, hours_worked: int):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def get_salary(self) -> str:
        month_salary = self.hours_worked * self.hours_worked * 15
        return f"Зарплата фрилансера {self.name} в месяц равна {month_salary}"

fulltime = FulltimeEmployee("Матвей", 80000)
freelance = Freelancer("Сергей", 800, 8)

print(fulltime.get_salary())
print(freelance.get_salary())

#Задача 4
class Pet(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def feed(self, food_weight: int) -> str:
        pass

class Dog(Pet):
    def __init__(self, name: str) -> str:
        super().__init__(name)

    def feed(self, food_weight: int):
        return f"{self.name} съел {food_weight} кг корма для собак"

class Hamster(Pet):
    def __init__(self, name: str):
        super().__init__(name)

    def feed(self, food_weight: int) -> str:
        return f"{self.name} сгрыз {food_weight} грамм зерен"

dog = Dog("Шарик")
hamster = Hamster("Вася")
print(dog.feed(3))
print(hamster.feed(700))