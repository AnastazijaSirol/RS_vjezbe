from aiohttp import web
import json

proizvodi = [
    {"naziv": "Laptop", "cijena": 1200, "kolicina": 5},
    {"naziv": "Mobitel", "cijena": 800, "kolicina": 10},
    {"naziv": "Tipkovnica", "cijena": 50, "kolicina": 20}
]

async def get_proizvodi(request):
    return web.Response(
        text=json.dumps(proizvodi),
        content_type="application/json"
    )

app = web.Application()
app.router.add_get("/proizvodi", get_proizvodi)

web.run_app(app, port=8081)

# curl http://localhost:8081/proizvodi