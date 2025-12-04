import aiohttp
import asyncio

'''async def fun(sesion: aiohttp.ClientSession):
    res = await sesion.get("https://jsonplaceholder.typicode.com/todos/1")
    rezultat = await res.json()
    return rezultat

async def main():
    async with aiohttp.ClientSession() as sesion:
        taks = [asyncio.create_task(fun(sesion)) for _ in range(5)]
        rez = await asyncio.gather(*taks)
        return rez'''

async def fun(sesion: aiohttp.ClientSession):
    try:
        res = await asyncio.wait_for (sesion.get("https://jsonplaceholder.typicode.com/todos/1"), timeout=2)
        rezultat = await res.json()
        return rezultat
    except asyncio.TimeoutError:
        print("Isteklo")
        return None

async def main():
    async with aiohttp.ClientSession() as sesion:
        taks = [asyncio.create_task(fun(sesion)) for _ in range(5)]
        rez = await asyncio.gather(*taks, return_exceptions=True)
        return rez

print(asyncio.run(main()))