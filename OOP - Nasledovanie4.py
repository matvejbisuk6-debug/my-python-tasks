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

