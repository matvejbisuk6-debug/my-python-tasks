#Задача 1
class Autentification:
    def __init__(self, name: str, password: int, token: int):
        self.name = name
        self.__password = password
        self.__token = token

    def login(self):
        return "Телеграмм успешно работает!"

    def change_password(self, old: int, new: int, new_token: int):
        if self.__password == new and self.__token:
            self.__password = new
            return f"{self.name} получил доступ к телеграмм боту"
        else:
            return f"{self.name} Доступ к телеграмм боту запрещен"

tg_bot = Autentification("Matvey", 171828, 373632828)
tg_bot.change_password(171828, 728272, 727727299)
print(tg_bot.login())