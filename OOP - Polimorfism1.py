#Задача 1
class Dog:
    def speak(self):
        return "Гав гав!"

class Cat:
    def speak(self):
        return "Мяу!"

class Cow:
    def speak(self):
        return "Му-у-у!"

def make_animal_speak(animal_object):
    print(animal_object.speak())

make_animal_speak(Dog())
make_animal_speak(Cat())
make_animal_speak(Cow())

#Задача 2
class TxtFile:
    def open_file(self):
        return "Открываю текстовый файл в блокноте"

class PdfFile:
    def open_file(self):
        return "Открываю PDF - файл в adobe reader"

class Mp3File:
    def open_file(self):
        return "Запускаю аудиофайл в плеере"

def make_file_open(file_object):
    print(file_object.open_file())

make_file_open(TxtFile())
make_file_open(PdfFile())
make_file_open(Mp3File())

#Задача 3
class Shape:
    def __init__(self, a: int):
        self.a = a

    def get_area(self):
        return 0

class Square(Shape):
    def __init__(self, a: int):
        super().__init__(a)

    def get_area(self):
        s1 = self.a * self.a
        return f"Площадь квадрата равна {s1} см2"

class Circle(Shape):
    def __init__(self, r: int, p: float):
        self.r = r
        self.p = p

    def get_area(self):
        s2 = self.p * (self.r * self.r)
        return f"Площадь круга равна {s2} см"

shapes = [Square(5), Circle(3, 3.14)]
for s in shapes:
    print(s.get_area())

#Задача 4
class CreditCardPayment:
    def pay(self, amount: int):
        return f"Оплачено {amount} рублей с банковской карты. Комиссия 2%"

class CryptioCardPayment(CreditCardPayment):
    def pay(self, amount: int):
        return f"Оплачено {amount} рублей в криптовалюте. Комиссия 0%"

class SbpPayment(CreditCardPayment):
    def pay(self, amount: int):
        return f"Оплачено {amount} рублей. По QR коду через СБП"

def payment(payment_object, amount: int):
    print(payment_object.pay(amount))

payment(CreditCardPayment(), 500)
payment(CryptioCardPayment(), 500)
payment(SbpPayment(), 500)