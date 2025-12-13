import asyncio
import json
from aiohttp import web, ClientSession

CATFACT_URL = "https://catfact.ninja/fact"

async def fetch_fact(session):
    async with session.get(CATFACT_URL) as resp:
        data = await resp.json()
        return data.get("fact")

async def get_cats(request):
    async with ClientSession() as session:
        tasks = [fetch_fact(session) for _ in range(5)]
        facts = await asyncio.gather(*tasks)
        return web.Response(
            text=json.dumps({"facts": facts}),
            content_type="application/json"
        )

async def get_cat_amount(request):
    try:
        amount = int(request.match_info["amount"])
        async with ClientSession() as session:
            tasks = [fetch_fact(session) for _ in range(amount)]
            facts = await asyncio.gather(*tasks)
            return web.Response(
                text=json.dumps({"facts": facts}),
                content_type="application/json"
            )
    except ValueError:
        return web.Response(
            text=json.dumps({"error": "Amount mora biti broj"}),
            content_type="application/json",
            status=400
        )

app = web.Application()
app.router.add_get("/cats", get_cats)
app.router.add_get("/cat/{amount}", get_cat_amount)

if __name__ == "__main__":
    web.run_app(app, port=8086)
