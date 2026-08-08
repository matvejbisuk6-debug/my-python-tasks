#Задача 1
class Counter:
    def __init__(self):
        self.value = 0

    def click(self):
        self.value += 1

    def reset(self):
        self.value = 0

    def get_value(self):
        return f"Текущее число равно {self.value}"

value = Counter()
print(value.get_value())

#Задача 2
class Student:
    def __init__(self, name: str):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        average = sum(self.grades) / len(self.grades)
        return f"Средний балл ученика {self.name} равен {average}."

student = Student("Matvey")
student.add_grade(5)
student.add_grade(4)
student.add_grade(5)
print(student.get_average())

#Задача 3
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def get_coordinates(self):
        return (self.x, self.y)

p = Point(5, 7)
p.move(3, -1)
print(p.get_coordinates())

#Задача 4
class Receipt:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price):
            self.items[item_name] = price

    def calc_total(self):
        return f"Общая сумма всех товаров равна {sum(self.items.values())}"

item = Receipt()
item.add_item("Хлеб", 50)
item.add_item("Вода", 60)
item.add_item("Молоко", 70)
print(item.calc_total())

#Задача 5
class Habit_tracker:
    def __init__(self, habit_name: str, target_days: int, current_streak: int):
        self.habit_name = habit_name
        self.target_days = target_days
        self.current_streak = current_streak

    def track_day (self):
        self.current_streak += 1

    def check_status(self):
        if self.target_days <= self.current_streak:
            return "Цель достигнута!"
        else:
            days = self.target_days - self.current_streak
            return f"Осталось дней: {days}"

habit_name = Habit_tracker("Пить 2 литра воды", 7, 0)
print(habit_name.check_status())


