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