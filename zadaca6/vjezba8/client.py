import asyncio
from aiohttp import ClientSession

async def fetch_catfacts(amount):
    async with ClientSession() as session:
        async with session.get(f"http://localhost:8086/cat/{amount}") as resp:
            return await resp.json()

async def check_catfacts(facts):
    async with ClientSession() as session:
        async with session.post("http://localhost:8087/facts", json=facts) as resp:
            return await resp.json()

async def main():
    facts = await fetch_catfacts(10)
    print("Činjenice o mačkama:", facts)

    filtered = await check_catfacts(facts)
    print("Filtrirane činjenice:", filtered)

if __name__ == "__main__":
    asyncio.run(main())
