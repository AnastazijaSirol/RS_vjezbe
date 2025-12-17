from aiohttp import web
from aiohttp.web import AppRunner, TCPSite
import asyncio, aiohttp

async def get_users(request):
    return web.json_response({'korisnici': ['Ivo', 'Ana', 'Marko', 'Maja', 'Iva', 'Ivan']})

app = web.Application()
app.router.add_get('/korisnici', get_users)

async def start_server():
    runner = AppRunner(app)
    await runner.setup()
    site = TCPSite(runner, 'localhost', 8080)
    await site.start()
    print("Poslužitelj sluša na http://localhost:8080")

async def main():
    asyncio.create_task(start_server())
    async with aiohttp.ClientSession() as session:
        print("Klijentska sesija otvorena")
        # Ovdje možemo poslati zahtjeve na server
        rezultat = await session.get('http://localhost:8080/korisnici')
        print(await rezultat.text())

asyncio.run(main())