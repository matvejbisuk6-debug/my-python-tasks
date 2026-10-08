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
