import json
from aiohttp import web

async def kolicnik(request):
    try:
        data = await request.json()
        zbroj = data.get("zbroj")
        umnozak = data.get("umnozak")

        if zbroj is None or umnozak is None:
            return web.Response(
                text=json.dumps({"error": "Nedostaju podaci zbroj ili umnozak"}),
                content_type="application/json",
                status=400
            )

        if zbroj == 0:
            return web.Response(
                text=json.dumps({"error": "Dijeljenje s nulom nije dozvoljeno"}),
                content_type="application/json",
                status=400
            )

        rezultat = umnozak / zbroj
        return web.Response(
            text=json.dumps({"kolicnik": rezultat}),
            content_type="application/json"
        )
    except Exception as e:
        return web.Response(
            text=json.dumps({"error": str(e)}),
            content_type="application/json",
            status=400
        )

app = web.Application()
app.router.add_post("/kolicnik", kolicnik)

if __name__ == "__main__":
    web.run_app(app, port=8085)
