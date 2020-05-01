import asyncio
import random

'''
Cервер возвращает ответы на запросы по мере готовности ответа.
Ответ на первый запрос может вернуться последним, если был "приготовлен" позже всех.
Запуск: python3.8 aserver.py
'''

async def server(r, w):
    data = await r.read(1024)
    rn = random.randint(2, 10)
    await asyncio.sleep(rn)
    w.write(b"Request number " + data + b". Answer was prepared in " + str(rn).encode() + b" seconds")
    await w.drain()
    w.close()


async def main():
    s = await asyncio.start_server(server, '127.0.0.1', 8000)
    async with s:
        await s.serve_forever()

try:
    asyncio.run(main())
except KeyboardInterrupt:
    pass
