import asyncio
import json
from aiohttp import web, ClientSession

proizvodi = [
    {"id": 1, "naziv": "Laptop", "cijena": 5000},
    {"id": 2, "naziv": "Miš", "cijena": 100},
    {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
    {"id": 4, "naziv": "Monitor", "cijena": 1000},
    {"id": 5, "naziv": "Slušalice", "cijena": 50}
]

async def get_proizvodi(request):
    return web.Response(
        text=json.dumps(proizvodi),
        content_type="application/json"
    )

async def get_proizvod(request):
    try:
        proizvod_id = int(request.match_info["id"])
        proizvod_lista = [p for p in proizvodi if p["id"] == proizvod_id]
        proizvod = proizvod_lista[0] if proizvod_lista else None

        if proizvod:
            return web.Response(
                text=json.dumps(proizvod),
                content_type="application/json"
            )
        else:
            return web.Response(
                text=json.dumps({"error": "Proizvod s traženim ID-em ne postoji"}),
                content_type="application/json",
                status=404
            )
    except ValueError:
        return web.Response(
            text=json.dumps({"error": "ID mora biti broj"}),
            content_type="application/json",
            status=400
        )

app = web.Application()
app.router.add_get("/proizvodi", get_proizvodi)
app.router.add_get("/proizvodi/{id}", get_proizvod)

async def start_server():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "localhost", 8081)
    await site.start()

async def main():
    await start_server()
    async with ClientSession() as session:
        resp = await session.get("http://localhost:8081/proizvodi")
        print("GET /proizvodi:", await resp.json())

        resp = await session.get("http://localhost:8081/proizvodi/3")
        print("GET /proizvodi/3:", await resp.json())

        resp = await session.get("http://localhost:8081/proizvodi/99")
        print("GET /proizvodi/99:", resp.status, await resp.json())

asyncio.run(main())
