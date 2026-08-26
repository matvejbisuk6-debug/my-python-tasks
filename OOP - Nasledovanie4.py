#Задача 1
class Character:
    def __init__(self, name: str, health: int, damage: int):
        self.name = name
        self.health = health
        self.damage = damage
        self.troll_killed = []

    def take_damage(self, troll_health: int, troll_damage: int, text: str):
        if troll_damage <= self.damage:
            self.troll_killed.append(text)
            return "Тролль 1 убит"
        elif troll_health > self.damage:
            self.health -= troll_damage
            return f"Тролль 1 наносит ответный удар у игрока {self.name} - {self.health} hp"
        else:
            self.troll_killed.append(text)
            return "Тролль 1 мертв"

class Mage(Character):
    def __init__(self, name: str, health: int, damage: int, mage: int):
        super().__init__(name, health, damage)
        self.mage = mage

    def take_damage(self, troll_health: int, troll_damage: int, text: str):
        new_damage = self.damage + self.mage
        if troll_damage <= new_damage:
            self.troll_killed.append(text)
            return "Тролль 2 убит"
        elif troll_health > new_damage:
            self.health -= troll_damage
            return f"Тролль 2 наносит ответный удар у игрока {self.name} - {self.health} hp"
        else:
            self.troll_killed.append(text)
            return "Тролль 2 мертв"

    def take_damage_boss(self, boss_health: int, boss_damage: int, text: str):
        new_damage = self.damage + self.mage
        if boss_health <= new_damage:
            self.troll_killed.append(text)
            return f"Босс убит, {self.troll_killed}"
        elif boss_health > self.damage:
            self.health -= boss_damage
            return f"Босс наносит ответный удар у игрока {self.name} - {self.health} hp"
        else:
            self.troll_killed.append(text)
            return f"Босс мертв, {self.troll_killed}"

character = Character("Matvey", 100, 5)
boss = Mage("Matvey", 100, 5, 20)
print(character.take_damage(5, 2, "Тролль1 убит"))
print(boss.take_damage(15, 5, "Тролль2 приспешник убит"))
print(boss.take_damage_boss(25, 25, "Король Троллей убит"))

#Задача 2
class User:
    def __init__(self, name: str, year_old: int):
        self.name = name
        self.year_old = year_old

class Base_Command(User):
    def __init__(self, name: str, year_old: int, command_start: bool):
        super().__init__(name, year_old)
        self.command_start = command_start

    def execute(self):
        if self.command_start == True and self.year_old >= 18:
            return f"Поздравляем! {self.name} Телеграмм бот запущен!"
        else:
            return "Error"

class SettingsCommand(User):
    def __init__(self, name: str, year_old: int, command_settings: str):
        super().__init__(name, year_old)
        self.command_settings = command_settings

    def execute(self):
        return f"Команда /settings включена, язык - {self.command_settings}"

class HelpCommand(User):
    def __init__(self, name: str, year_old: int, help_command: bool):
        super().__init__(name, year_old)
        self.help_command = help_command

    def execute(self, text: str):
        if self.help_command == True and self.year_old >= 18:
            return f"Поздравляем, {self.name}! Завтра мы поможем вам {text}"
        else:
            return "Мы не поможем вам."

base = Base_Command("Matvey", 19, True)
setting = SettingsCommand("Matvey", 19, "Немецкий")
help = HelpCommand("Matvey", 19, True)
print(base.execute())
print(setting.execute())
print(help.execute("помириться с другом"))