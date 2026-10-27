import functools
import asyncio

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
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{func.__name__}Функция начинает работу")
        result = func(*args, **kwargs)
        return result
    return wrapper

@logger
def name():
    return "Первая"

print(name())

#Задача 4
async def main():
    print("SELECT запрос в базу данных отправлен")
    await asyncio.sleep(2)
    print("Отправка завершена")

asyncio.run(main())