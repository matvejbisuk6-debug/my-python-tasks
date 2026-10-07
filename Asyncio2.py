import asyncio
import random


#Задача 1
async def process_payment(user, amount):
    print(f"{user}: Начало оплаты счета на {amount} рублей")
    await asyncio.sleep(1.5)
    print(f"{user}: Оплата успешно проведена!")

async def main():
    result1 = await process_payment("Иван", 100)
    print(result1)
    result2 = await process_payment("Анна", 500)
    print(result2)
    result3 = await process_payment("Петр", 1200)
    print(result3)
    result4 = await process_payment("Виктория", 2000)
    print(result4)

asyncio.run(main())

#Задача 2
async def ping_server(server_name, ip):
    print(f"Имя сервера {server_name} и адрес {ip} приняты и установлены")
    random.uniform(0.5, 2.0)
    return f"Сервер {server_name} ({ip}) доступен"

async def main():
    results = await asyncio.gather(
        ping_server("Yandex", "1k.2k.3k.4k"),
        ping_server("Google", "8.8.8.8"),
        ping_server("GitHub", "140.82.121.4"),
        ping_server("Mail", "94.100.180.201"),
    )
    print(results)

asyncio.run(main())

#Задача 3
async def parse_page(page_num):
    print("Интернет страница магазина, скачивается")
    await asyncio.sleep(1)
    return [{"id": 1, "name": "Товар 1"}]

async def main():
    tasks = await  asyncio.gather(
        parse_page([])
    )
import random


#Задача 1
async def process_payment(user, amount):
    print(f"{user}: Начало оплаты счета на {amount} рублей")
    await asyncio.sleep(1.5)
    print(f"{user}: Оплата успешно проведена!")

async def main():
    result1 = await process_payment("Иван", 100)
    print(result1)
    result2 = await process_payment("Анна", 500)
    print(result2)
    result3 = await process_payment("Петр", 1200)
    print(result3)
    result4 = await process_payment("Виктория", 2000)
    print(result4)

asyncio.run(main())

#Задача 2
async def ping_server(server_name, ip):
    print(f"Имя сервера {server_name} и адрес {ip} приняты и установлены")
    random.uniform(0.5, 2.0)
    return f"Сервер {server_name} ({ip}) доступен"

async def main():
    results = await asyncio.gather(
        ping_server("Yandex", "1k.2k.3k.4k"),
        ping_server("Google", "8.8.8.8"),
        ping_server("GitHub", "140.82.121.4"),
        ping_server("Mail", "94.100.180.201"),
    )
    print(results)

asyncio.run(main())

#Задача 3
async def parse_page(page_num):
    print(f"Интернет страница магазина {page_num}, скачивается")
    await asyncio.sleep(1)
    return [{"id": {page_num}, "name": "Товар 1"}]

async def main():
    tasks = ["Товар2", "Товар3", "Товар4", "Товар5", "Товар6"]
    for i in tasks:
        results = await asyncio.gather(
           parse_page(2),
           parse_page(3),
           parse_page(4),
           parse_page(5),
           parse_page(6)
        )
        print(results)

asyncio.run(main())

#Задача 3
async def background_logger():
    while True:
         print("---Система работает стабильно---")
         await asyncio.sleep(2)
         print("---Система засыпает---")


async def main():
    logger_task = asyncio.create_task(background_logger())
    asyncio.run(main())
    print("Какие-то данные скачиваются")
    await  asyncio.sleep(5)
    logger_task.cancel()

if __name__ == "__main__":
    asyncio.run(main())

#Задача 5
async def fetch_api(source_name):
    if source_name == "Сервер 3":
        return f"Ошибка подключения к серверу{source_name}"
    else:
        await asyncio.sleep(1)
        return f"Данные от {source_name}"

async def main():
    sources_list = ["Сервер 1","Сервер 2", "Сервер 3", "Сервер 4"]
    tasks = [fetch_api(source) for source in sources_list]
    result = await asyncio.gather(*tasks, return_exceptions=True)
    for source in result:
        if source != "Сервер":
            return f"Запрос к источнику провален: {source}"
        else:
            return source

if __name__ == "__main__":
    asyncio.run(main())
