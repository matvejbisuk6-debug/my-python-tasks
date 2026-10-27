import functools

#Задача 1
for i in range(1, 100):
    i //= 3
    if i % 3 == 0:
        print("Python")
    elif i % 5 == 0:
        print("SQL")
    else:
        print("Backend")

#Задача 2
class City:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def upgrade_infrastructure(self):

        new_population = self.population + (self.population * 0.10)
        return f"Старое населние города {self.name} равно {self.population},новое население города {self.name} равно {new_population}"

Yaroslavl = City("Ярославль", 563000)
Pereslavl_Zalessky = City("Переславль-Залесский", 35000)
print(Yaroslavl.upgrade_infrastructure())
print(Pereslavl_Zalessky.upgrade_infrastructure())

#Задача 3
def logger(func):
    def wrapper():
