#Задача 1
class CleaningRobot:
    def work(self, clener_robot: str):
        return f"Робот {clener_robot} пылесосит ковер и моет пыль"

class CookingRobot:
    def work(self, cooking_robot: str):
        return f"Робот {cooking_robot} нарезает овощи и варит суп"

class SecurityRobot:
    def work(self, security_robot: str):
        return f"Робот {security_robot} сканирует периметр на наличие нарушителей"

def start_shift():
    robots_list = [CleaningRobot(), CookingRobot(), SecurityRobot()]

    for robot in robots_list:
        print(robot.work("Марк-1"))

start_shift()

#Задача 2
class AudioTrack:
    def play(self):
        return "Воспроизведение звука через динамики"

class VideoTrack:
    def play(self):
        return "Вывод видео на экран + звук"

class SubtitleTrack:
    def play(self):
        return "Отображение текста субтитров внизу экрана"

def tracks():
    movie_list = [AudioTrack(), VideoTrack(), SubtitleTrack()]

    for track in movie_list:
        print(track.play())

tracks()

#Задача 3
class Herbivore:
    def __init__(self, food: str):
        self.food = food

    def eat(self):
        if self.food == "Трава":
            return "животное с аппетитом жует траву"
        else:
            return "Животное отказывается это есть"

class Carnivore:
    def __init__(self, food: str):
        self.food = food

    def eat(self):
        if self.food == "Мясо":
            return "Хищник съедает свою добычу"
        else:
            return "ищник не ест расстения"

def animals():
    eat_list = [Herbivore("Трава"), Carnivore("Мясо")]

    for eat in eat_list:
        print(eat.eat())

animals()

#Задача 4
class WoodenDoor:
    def __init__(self, item: str):
        self.item = item

    def try_open(self):
        if self.item == "ключ":
            return True
        else:
            return False

class CodeDoor:
    def __init__(self, item: str):
        self.item = item

    def try_open(self):
        if self.item == "пароль":
            return True
        else:
            return False

class MagicDoor:
    def __init__(self, item: str):
        self.item = item

    def try_open(self):
        if self.item == "заклинание":
            return True
        else:
            return False

def doors():
    door_list = [WoodenDoor("ключ"), CodeDoor("пароль"), MagicDoor("заклинание")]

    for door in door_list:
        print(door.try_open())

doors()

#Задача 5
class UserReport:
    def generate(self):
        return {"title": "Отчет по пользователям", "count": 150}

class SalesReport:
    def generate(self):
        return {"title": "Отчет по продажам", "total_revenue": 45000}

class BugReport:
    def generate(self):
        return {"title": "Отчет по ошибкам", "critical": 2, "minor": 12}

class AnalyticsDashboard:
    def show_all_times(self):
        report_list = [UserReport(), SalesReport(), BugReport()]

        for report in report_list:
            print(report.generate()["title"])

dashboard = AnalyticsDashboard()
dashboard.show_all_times()
