#Задача 1
class LengthValidator:
    def __init__(self, min_len: int, max_len: int):
        self.min_len = min_len
        self.max_len = max_len

    def validate(self, value: str):
        if self.min_len <= len(value) and self.max_len > len(value):
            return True
        else:
            return False

class TypeValidator:
    def __init__(self, expected_type: type):
        self.expected_type = (expected_type
                         )

    def validate(self, value: str):
        try:
            self.expected_type(value)
            return True
        except(ValueError):
            return False

class Form:
    def check_field(self, field_name, value):
        validate_list = [LengthValidator(1, 10), TypeValidator(int)]

        for val in validate_list:
           print(val.validate(value))

check = Form()
check.check_field("age", "5")

#Задача 2
class UpperFormatter:
    def __init__(self, text: str):
        self.text = text

    def format_text(self):
        self.text.upper()
        return self.text

class BorderFormatter:
    def __init__(self, text:str):
        self.text = text

    def format_text(self):
        return f"*** {self.text} ***"

class ReverseFormatter:
    def __init__(self, text: str):
        self.text = text

    def format_text(self):
        reversed_text = self.text[::-1]
        return reversed_text

class ChainFormatter:
    def format_text(self, text):
        format_list = [UpperFormatter("Привет"), BorderFormatter("Здорова"), ReverseFormatter("Хай")]

        for format in format_list:
            print(format.format_text())

chain = ChainFormatter()
chain.format_text("Привет")

#Задача 3
class Character:
    def __init__(self, name: str, hp: int, attack_power: int):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.active_auras = []

class PoisonAura:
    def apply(self, character: str):
        character.hp -= 10
        return f"{character} получает 10 урона от яда, остается {character.hp} хп"

class RegenAura:
    def apply(self, character):
        character.hp += 15
        return f"{character} получает 15 хп, по итогу {character.hp} хп"

class RageAura:
    def apply(self, character):
        character.hp -= 5
        character.attack_power += 5
        return  (f"{character} Получает 5 урона, остается {character.hp} хп, но урон игрока {character} равен {character.attack_power}")

def end_of_turn():
    hero = Character(name="Матвей", hp=100, attack_power=20)
    aura_list = [PoisonAura(), RegenAura(), RageAura()]

    for aura in aura_list:
        print(aura.apply(hero))

end_of_turn()

#Задача 4
class BrightnessFilter:
    def __init__(self, delta: int):
        self.delta = delta

    def apply_filter(self, pixels: int):
        pixels += self.delta
        if pixels > 255:
            return "Error"
        else:
            return "True"

class InvertFilter:
    def __init__(self, x: int):
        self.x = x

    def apply_filter(self, pixels: int):
        self.x = pixels
        return f"Количество пикселей равно {self.x}"

class BlurFilter:
    def __init__(self, pixel1: int, pixel2: int, pixel3: int):
        self.pixel1 = pixel1
        self.pixel2 = pixel2
        self.pixel3 = pixel3

    def apply_filter(self, pixel=None):
        medium = (self.pixel1 + self.pixel2 + self.pixel3) / 3
        if medium <= 255:
            return f"Блюр пискселей равен {medium}"
        else:
            return "Error"

def photo_filter():
    filter_list = [BrightnessFilter(100), InvertFilter(200), BlurFilter(100, 50, 50)]

    for filter in filter_list:
        print(filter.apply_filter(100))

photo_filter()