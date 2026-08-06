#Задача 1
import builtins
from locale import currency


class Calorie_calculator:
    def __init__(self, name: str, calory_norm: int, calories: int):
        self.name = name
        self.calory_norm = calory_norm
        self.calories = calories

    def add_food(self, calories):
        self.calories += calories
        print(f"Вами было съедено {self.calories} калорий за весь день")

    def get_remaining(self):
        if self.calories < self.calory_norm:
            remainder = self.calory_norm - self.calories
            return f"Вам надо добрат {remainder} калорий"
        else:
            return 0

people1 = Calorie_calculator("Matvey", 2300, 300)
people1.add_food(400)
print(people1.get_remaining())

#Задача 2
class wallet:
    def __init__(self, currency: str, balance: int, amount: int):
        self.currency = currency
        self.balance = balance
        self.amount = amount

    def deposit(self, amount):
        self.balance += amount
        print(f"Итого ваш увеличенный баланс равен {self.balance} долларов")

    def withdraw(self):
        if self.balance > self.amount:
            new_balance = self.balance - self.amount
            return (f"На балансе {new_balance} долларов, деньги есть")
        else:
            return "недостаточно средств"

currency = wallet("USD", 1000, 300)
print(currency.withdraw())

#Задача 3
class CinemaHall:
    def __init__(self, seats_per_row: int, rows: int):
        self.hall = [[0 for _ in range(seats_per_row)] for _ in range(rows)]

    def book_seat(self, row, seat):
        if self.hall[row - 1][seat - 1] == 0:
            self.hall[row - 1][seat - 1] = 1
            return True
        else:
            return False

    def free_seats_count(self):
        return sum(row.count(0) for row in self.hall)

hall = CinemaHall(5, 10)
print(hall.free_seats_count())

#Задача 4
class Product:
    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

class Warehouse:
    def __init__(self):
        self.warehouse = {}

    def add_product(self, name, price, quantity):
        if name in self.warehouse:
            self.warehouse[price] += quantity
        else:
            self.warehouse[price] = quantity

    def get_total_value(self, product):
        total = product.price * product.quantity
        return f"Итоговая стоимость товара равна {total} рублей"

name = Product("pen", 80, 3)
my_warehouse = Warehouse()
print(my_warehouse.get_total_value(name))

#Задача 5
class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def print_info(self):
        return f"Книга: {self.title}, Автор: {self.author}, Количество страниц {self.pages}"

title = Book("Капитанская дочка", "А.С Пушкин", 160)
print(title.print_info())