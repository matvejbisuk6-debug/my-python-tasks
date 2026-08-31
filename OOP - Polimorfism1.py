#Задача 5
class Fireball:
    def __init__(self, hp: int):
        self.hp = hp

    def cast(self, target_hp: int):
        self.hp -= target_hp
        return f"Огненный шар наносит 50 урона, осталось по итогу {self.hp}"

class Heal(Fireball):
    def __init__(self, hp: int):
        super().__init__(hp)

    def cast(self, target_hp: int):
        self.hp += target_hp
        return  f"Лечение восстанавливает 40 здоровья, по итогу у вас {self.hp}"

class Freeze(Fireball):
    def __init__(self, hp: int):
        super().__init__(hp)

    def cast(self):
        return "Цель заморожена на 1 ход"

fireball = Fireball(100)
heal = Heal(100)
freeze = Freeze(100)
print(fireball.cast(50))
print(heal.cast(40))
print(freeze.cast())

#Задача 6
class Button:
    def render(self):
        return "[ Кнопка ]"

class InputField:
    def render(self):
        return "[ Введите текст ]"

class Checkbox:
    def render(self):
        return "[ [x] Чекбокс ]"

class Window:
    def __init__(self, name: str):
        self.name = name
        self.widgets = []

    def add_widget(self, widget: str):
        self.widgets.append(widget)
        return self.widgets

    def render(self):
        return f"Название окна - {self.name}"

button = Button()
input = InputField()
checkbox = Checkbox()
window = Window("Pycharm")
print(button.render())
print(input.render())
print(checkbox.render())
print(window.add_widget("Время"))
print(window.render())