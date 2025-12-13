import json
from aiohttp import web

async def check_facts(request):
    try:
        data = await request.json()
        facts = data.get("facts", [])
        filtered = [fact for fact in facts if "cat" in fact.lower()]
        return web.Response(
            text=json.dumps({"filtered_facts": filtered}),
            content_type="application/json"
        )
    except Exception as e:
        return web.Response(
            text=json.dumps({"error": str(e)}),
            content_type="application/json",
            status=400
        )

app = web.Application()
app.router.add_post("/facts", check_facts)

if __name__ == "__main__":
    web.run_app(app, port=8087)
