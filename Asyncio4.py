import asyncio

#Задача 1
async def get_user_input():
    await asyncio.sleep(3)
    return "Правильный ответ"

async def main():
    task = asyncio.create_task(get_user_input())

    try:
        result = await asyncio.wait_for(task , timeout=3.0)
        print(f"Ответ принят! Вы заработали 10 очков.(Получено: {result})")

    except asyncio.TimeoutError:
        print("Время вышло! Вы не успели ответить.")

if __name__ == "__main__":
    asyncio.run(main())

#Задача 2
async def download_file(file_name, file_size):
    downloaded_bytes = 0
    while downloaded_bytes < file_size:
        downloaded_bytes += 10
        await asyncio.sleep(0.5)
        print(f"Файл {file_name}: скачано {downloaded_bytes}%")

async def main_download():
    download_list = await asyncio.gather(
        download_file("Видео.mp4", 100),
        download_file("Музыка.mp3", 50),
        download_file("Документ.pdf", 20)
    )

if __name__ == "__main__":
    asyncio.run(main_download())

#Задача 3
async def new_stream(num, news_name):
    while True:
        await asyncio.sleep(1.5)
        print(f"Новость №{num}, название {news_name}")

async def news_main():
    stream1 = asyncio.create_task(new_stream("Война", 1))
    stream2 = asyncio.create_task(new_stream("Улучшение экономики", 2))
    stream3 = asyncio.create_task(new_stream("Вышла новая игра", 3))

    await asyncio.sleep(5)
    stream1.cancel()
    stream2.cancel()
    stream3.cancel()

if __name__ == "__main__":
    asyncio.run(news_main())

#Задача 4
async def fetch_metrics(server_id, download):
    if server_id == 2:
        await asyncio.sleep(100)
    elif server_id == 4:
        print("ConnectionError")
    else:
        return download

async def download_main():
    


