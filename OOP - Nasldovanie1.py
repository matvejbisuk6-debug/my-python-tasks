#Задача 1
from itertools import product

from peremennye2 import discount


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return f"*{self.name} издает звук"

class Dog(Animal):
    def make_sound(self):
        return f"{self.name} лает: Гав!"

class Cat(Animal):
    def make_sound(self):
        return f"{self.name} мяукает: Мяу!"

dog = Dog("Рекс")
cat = Cat("Барсик")
print(dog.make_sound())
print(cat.make_sound())

#Задача 2
class User:
    def __init__(self, username: str):
        self.username = username

    def watch_video(self):
        return "Просмотр видео с рекламой"

class PremiumUser(User):
    def watch_video(self):
        return "Просмотр видео без рекламы в 4К качестве"

    def download_video(self):
        return "Видео скачивается..."

top_user = PremiumUser("Matvey")
print(top_user.watch_video())

#Задача 3
class Venicle:
    def __init__(self, brand: str, speed: int):
        self.brand = brand
        self.speed = speed

    def drive(self):
        return f"{self.brand} едет со скоростью {self.speed} км/ч"

class ElectricCar(Venicle):
    def __init__(self, brand: str, speed: int, battery_capacity: int):
        super().__init__(brand, speed)
        self.battery_capacity = battery_capacity

    def show_battery(self):
        return f"Емкость батареи равна {self.battery_capacity} %"

venicle = Venicle("Tesla", 80)
car = ElectricCar("Tesla", 80, 100)
print(venicle.drive())
print(car.show_battery())

#Задача 4
class Employee:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name: str, salary: int, bonus: str):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_total_income(self):
        new_salary = self.bonus + self.salary
        return f"Зарплата сотрудника {self.name} равна {new_salary} рублей "

emplayee = Employee("Матвей", 80000)
manager = Manager("Матвей", 80000, 20000)
print(manager.get_total_income())

#Задача 5
class Product:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def get_price(self, quantity: int):
        all_price = quantity * self.price
        return f"Стандатная цена без скидки - {all_price} рублей"

class Discount_product(Product):
    def __init__(self, name: str, price: int, discount: float):
        super().__init__(name, price)
        self.discount = discount

    def get_price(self, quantity: int):
        all_price = quantity * self.discount * self.price
        return f"Цена товара со скидкой {self.discount} равна {all_price} рублей"

product = Product("Творог", 120)
discount = Discount_product("Творог", 120, 0.20)
print(discount.get_price(3))
print(product.get_price(3))

#Задача 6
class Character:
    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp

    def take_damage(self, damage: int):
        self.hp -= damage
        if self.hp <= 0:
            return f"{self.name} погиб"

class ArmoredCharacter(Character):
    def __init__(self, name: str, hp: int,armor: int):
        super().__init__(name, hp)
        self.armor = armor

    def take_damage(self, damage: int):
        if self.armor >= damage:
            return f"Игрок {self.name} имеет броню {self.armor} и {self.hp} количество жизней"
        else:
            self.hp -= damage
            return f"Игрок {self.name} имеет броню {self.armor} и {self.hp} количество жизней"

character = Character("Matvey", 100)
armored_character = ArmoredCharacter("Matvey", 100, 10)
print(character.take_damage(9))
print(armored_character.take_damage(9))