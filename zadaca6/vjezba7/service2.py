import json
from aiohttp import web
import math

async def umnozak(request):
    try:
        data = await request.json()
        brojevi = data.get("brojevi")
        if not brojevi:
            return web.Response(
                text=json.dumps({"error": "Lista brojeva nije proslijeđena"}),
                content_type="application/json",
                status=400
            )
        rezultat = math.prod(brojevi)
        return web.Response(
            text=json.dumps({"umnozak": rezultat}),
            content_type="application/json"
        )
    except Exception as e:
        return web.Response(
            text=json.dumps({"error": str(e)}),
            content_type="application/json",
            status=400
        )

app = web.Application()
app.router.add_post("/umnozak", umnozak)

if __name__ == "__main__":
    web.run_app(app, port=8084)
