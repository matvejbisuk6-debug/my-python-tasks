#Задача 1
from os import remove


class Player:
    def __init__(self, nickname: str, level: int, clan:int):
        self.nickname = nickname
        self.level = level
        self.clan = clan

    def level_up(self):
        self.level += 1

    def show_profile(self):
        return f"Мгрок {self.nickname} из клана {self.clan} имеет {self.level} уровень"

player = Player("Motya_0212", 93, "Русский")
print(player.show_profile())

#Задача 2
class Kettle:
    def __init__(self):
        self.water_level = 0
        self.is_boiling = False

    def fill_water(self, liters):
        self.water_level += liters

    def turn_on(self):
        if self.water_level > 0:
            self.is_boiling = True
            return self.is_boiling
        else:
            self.is_boiling = False
            return "Ошибка чайник пуст"

water = Kettle()
water.fill_water(5)
print(water.turn_on())

#Задача 3
class Playlist:
    def __init__(self, name: str):
        self.name = name
        self.songs = []

    def add_song(self, song_title):
        self.songs.append(song_title)

    def show_playlist(self):
        if self.songs:
            return self.songs
        else:
            return f"Плейлист {self.name} пуст"

song = Playlist("Любимая музыка")
song.add_song("Rammstein Sohne")
song.add_song("Гимн Российской империи")
song.add_song("Цой Группа Крови")
print(song.show_playlist())

#Задача 4
class Car:
    def __init__(self, max_speed: int, current_speed: int):
        self.max_speed = max_speed
        self.current_speed = current_speed

    def accelerate(self, speed_increace):
        self.current_speed += speed_increace
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def brake(self):
        self.current_speed = 0
speed = Car(250, 140)
speed.accelerate(50)
print(speed.brake())

#Задача 5
class TodoList:
    def __init__(self):
        self.completed = []
        self.tasks = []

    def add_task(self, task_name):
        self.tasks.append(task_name)

    def complete_task(self, task_name):
        if task_name in self.tasks:
            self.tasks.remove(task_name)
            self.completed.append(task_name)
            return "Выполнена"
        else:
            return "Задача не найдена"

    def get_status_report(self):
        completed_count = len(self.completed)
        incompleted_count = len(self.tasks)
        return (completed_count, incompleted_count)

list = TodoList()
list.add_task("Купить хлеб")
list.add_task("Сходить погулять")
list.add_task("Заняться программированием")

print(list.get_status_report())

list.add_task("Сходить погулять")
list.add_task("Заняться программированием")

print(list.get_status_report())