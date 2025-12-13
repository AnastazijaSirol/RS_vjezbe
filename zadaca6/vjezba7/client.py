import asyncio
from aiohttp import ClientSession

async def fetch(url, port, payload):
    async with ClientSession() as session:
        async with session.post(f"http://localhost:{port}{url}", json=payload) as resp:
            return await resp.json()

async def main():
    payload = {"brojevi": [2, 3, 4]}

    print("Konkurentno")
    results = await asyncio.gather(
        fetch("/zbroj", 8083, payload),
        fetch("/umnozak", 8084, payload)
    )

    zbroj_result = results[0].get("zbroj")
    umnozak_result = results[1].get("umnozak")
    print("Rezultat zbroja:", zbroj_result)
    print("Rezultat umnoška:", umnozak_result)

    print("\nSekvencijalno")
    payload_div = {"zbroj": zbroj_result, "umnozak": umnozak_result}
    rezultat_div = await fetch("/kolicnik", 8085, payload_div)
    print("Rezultat količnika:", rezultat_div)

if __name__ == "__main__":
    asyncio.run(main())
