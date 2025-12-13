from aiohttp import web
import json

korisnici = [
    {'ime': 'Ivo', 'godine': 25},
    {'ime': 'Ana', 'godine': 17},
    {'ime': 'Marko', 'godine': 19},
    {'ime': 'Maja', 'godine': 16},
    {'ime': 'Iva', 'godine': 22}
]

async def get_punoljetni(request):
    punoljetni = [k for k in korisnici if k['godine'] >= 18]
    return web.Response(
        text=json.dumps(punoljetni),
        content_type="application/json"
    )

app = web.Application()
app.router.add_get("/punoljetni", get_punoljetni)

web.run_app(app, port=8082)

# curl http://localhost:8082/punoljetni