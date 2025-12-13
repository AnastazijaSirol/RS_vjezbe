import json
from aiohttp import web

async def zbroj(request):
    try:
        data = await request.json()
        brojevi = data.get("brojevi")
        if not brojevi:
            return web.Response(
                text=json.dumps({"error": "Lista brojeva nije proslijeđena"}),
                content_type="application/json",
                status=400
            )
        rezultat = sum(brojevi)
        return web.Response(
            text=json.dumps({"zbroj": rezultat}),
            content_type="application/json"
        )
    except Exception as e:
        return web.Response(
            text=json.dumps({"error": str(e)}),
            content_type="application/json",
            status=400
        )

app = web.Application()
app.router.add_post("/zbroj", zbroj)

if __name__ == "__main__":
    web.run_app(app, port=8083)
