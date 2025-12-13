import asyncio
import json
from aiohttp import web

async def pozdrav(request):
    await asyncio.sleep(4)
    return web.Response(
        text=json.dumps({"message": "Pozdrav nakon 4 sekunde"}),
        content_type="application/json"
    )

app = web.Application()
app.router.add_get("/pozdrav", pozdrav)

if __name__ == "__main__":
    web.run_app(app, port=8082)
