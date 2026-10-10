import asyncio
from asyncio import FIRST_COMPLETED
from tkinter.font import names


#Задача 1
async def download_page(page_id, semaphore):

    async with semaphore:
         print(f"Старт, скачиваю страницу {page_id}")
         await asyncio.sleep(1)
         print(f"Финиш, страница {page_id} скачана")

async def main():
    sem = asyncio.Semaphore(3)

    tasks = [download_page(page_id, sem) for page_id in range(1, 11)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())

#Задача 2
async def lucky_user(name):
    print(name)
    await asyncio.sleep(1, 5)
    print(name)

async def main():
    names = ["Алексей", "Мария", "Иван", "Елена"]
    tasks = [asyncio.create_task(lucky_user(name)) for name in names]
    result, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    for task in pending:
        task.cancel()

    await asyncio.sleep(0.1)

if __name__ == "__main__":
    asyncio.run(main())

#Задача 3
async def order_producer(queue):
    orders = ["Заказ №1", "Заказ №2", "Заказ №3", "Заказ №4", "Заказ №5"]
    for order in orders:
        await queue.put(order)
    await asyncio.sleep(1)

async def order_worker(queue):
    while True:
        order = await queue.get()
        await asyncio.sleep(1.5)
        print(f"Заказ {order} успешно обработан")
        queue.task_done()

async def main_3():
    queue = asyncio.Queue()

    producer = asyncio.create_task(order_producer(queue))
    worker = asyncio.create_task(order_worker(queue))

    await queue.join()

    worker.cancel()

if __name__ == "__main__":
    asyncio.run(main_3())

#Задача 4
async def generate_report():
    try:
        print("Файл генерируется...")
        await asyncio.sleep(4)
    except asyncio.CancelledError:
        print("Генерация прервана")
        raise

async def main():
    task = asyncio.create_task(generate_report())

    await asyncio.sleep(2)

    try:
        task.cancel()
        await task
    except asyncio.CancelledError:
        print("Генерация отчета успешно отменена пользователем, ресурсы свободны.")

if __name__ == "__main__":
    asyncio.run(main())

#Задача 5
async def fetch_news(delay, news_list):
    await asyncio.sleep(delay)
    return news_list

async def edit_news():
    edit_list = await asyncio.gather(
        fetch_news(1, ["Погода", "Спорт"]),
        fetch_news(2, ["Политика", "Кризис", "Экономика"])
    )

    results = edit_list[0] + edit_list[1]
    if "Кризис" in results:
        results.remove("Кризис")
    print(results)
    return results


if __name__ == "__main__":
    asyncio.run(main())