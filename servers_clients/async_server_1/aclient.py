import asyncio

'''
Клиент для асинхронного сервера. Отправляет сразу несколько запросов.
В теле запроса указан "номер" запроса. Благодяря номеру можно понять,
на какой запрос сервер уже ответил, а на какой - нет.
Запуск: python3.8 aclient.py
'''

async def client(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8000)

    writer.write(str(message).encode())
    print(message)
    data = await reader.read(1024)

    print(data.decode())
    writer.close()

async def main():
    await asyncio.gather(*[client(i) for i in range(5)])

asyncio.run(main())