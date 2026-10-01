import asyncio

#Задача 1
async def counter(name, seconds):
    print(f"{name}: осталось {seconds} секунд")
    await asyncio.sleep(1)
    print(f"{name}: время вышло")

async def main():
    result = await counter("Часы", 5)
    print(f"Результат: {result}")

asyncio.run(main())

#Задача 2
async def db_connect(name):
    print(f"{name} выполняет подключение к базе данных")
    await asyncio.sleep(1)
    return True
async def get_users(list):
    await asyncio.sleep(2)
    list.extend(["Матвей", "Екатерина"])
    return list

async def main():
    result1 = await db_connect("no name")
    print(f"Результат: {result1}")
    if result1 == True:
        result2 = await get_users([])
        print(f"Результат: {result2}")

asyncio.run(main())

#Задача 3
async def download_site(url, delay):
    await asyncio.sleep(delay)
    return f"Данные с {url} загружены"

async def main():
    result1 = await download_site("github.com", 1)
    print(f"Итого: {result1}")
    result2 = await download_site("vk.com", 2)
    print(f"Итого: {result2}")
    result3 = await download_site("google.com", 3)
    print(f"Итого: {result3}")

asyncio.run(main())

#Задача 4
async def deliver_pizza(order_id, time_to_cook):
    print(f"пицца {order_id} готовится")
    await asyncio.sleep(time_to_cook)
    print(f"Пицца {order_id} доставлена")

async def main():
    result1 = await deliver_pizza("пепперони", 1)
    print(result1)
    result2 = await deliver_pizza("грибная", 2)
    print(result2)
    result3 = await deliver_pizza("Охотничья", 3)
    print(result3)

asyncio.run(main())

#Задача 5
async def heavy_calculation():
    print("Имитирую сложный процесс")
    await asyncio.sleep(10)
    print("Имитация завершена")

async def main():
    try:
        print("Запускаем задачу с лимитом в 3 секунды")
        result = await asyncio.wait_for(heavy_calculation(), timeout=3)
        print(f"Успех! Получено: {result}")

    except asyncio.TimeoutError:
        print("Ошибка:время ожидания ответа истекло! Задача выполнилась слишком долго")

    except Exception as e:
        print(f"Произошла другая ошибка: {e}")

asyncio.run(main())