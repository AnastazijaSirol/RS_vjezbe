import asyncio
import aiohttp
import time

async def fetch_users(sesion: aiohttp.ClientSession):
    async with sesion.get("https://jsonplaceholder.typicode.com/users") as rezultat: 
        users = await rezultat.json()
    ime = [user["name"] for user in users]
    email = [user["email"] for user in users]
    username = [user["username"] for user in users]
    return ime, email, username

async def main():
    async with aiohttp.ClientSession() as sesion:
        rez = [asyncio.create_task(fetch_users(sesion)) for i in range(5)]
        useri = await asyncio.gather(*rez)
        print(useri)

t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()

print(f"Vrijeme: {round(t2-t1, 2)}")