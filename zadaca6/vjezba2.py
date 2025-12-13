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

async def post_proizvodi(request):
    try:
        data = await request.json()
        print("Primljeni podaci:", data)

        proizvodi.append({
            "naziv": data.get("naziv"),
            "cijena": data.get("cijena"),
            "kolicina": data.get("kolicina")
        })

        return web.Response(
            text=json.dumps(proizvodi),
            content_type="application/json"
        )
    except Exception as e:
        return web.Response(
            text=json.dumps({"error": str(e)}),
            content_type="application/json",
            status=400
        )

app = web.Application()
app.router.add_get("/proizvodi", get_proizvodi)
app.router.add_post("/proizvodi", post_proizvodi)

web.run_app(app, port=8081)

# curl -X POST http://localhost:8081/proizvodi -H "Content-Type: application/json" -d "{\"naziv\": \"Monitor\", \"cijena\": 300, \"kolicina\": 7}"
# curl http://localhost:8081/proizvodi
