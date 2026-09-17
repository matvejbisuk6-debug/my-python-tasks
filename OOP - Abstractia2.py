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

#Задача 2
class AuthService(ABC):

    @abstractmethod
    def login(self, username: str, password: int) -> None:
        pass

class PasswordAuth(AuthService):

    def login(self, username: str, password: str) -> str:
        if password == "1234":
            return True
        else:
            return False

class SmsCodeAuth(AuthService):

    def login(self, username: str, password: str) -> str:
        if len(password) == 4:
            return True
        else:
            return False

password_auth = PasswordAuth()
sms_auth = SmsCodeAuth()

print(password_auth.login("Matvey", "1234"))
print(sms_auth.login("Matvey", "1234"))