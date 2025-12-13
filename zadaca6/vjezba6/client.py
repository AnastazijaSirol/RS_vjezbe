import asyncio
from aiohttp import ClientSession

async def fetch_pozdrav(url, port):
    async with ClientSession() as session:
        async with session.get(f"http://localhost:{port}{url}") as resp:
            return await resp.json()

async def main():
    odgovor1 = await fetch_pozdrav("/pozdrav", 8081)
    print("Odgovor sa servisa 1:", odgovor1)

    odgovor2 = await fetch_pozdrav("/pozdrav", 8082)
    print("Odgovor sa servisa 2:", odgovor2)

    print("\nKonkurentno:")
    tasks = [
        fetch_pozdrav("/pozdrav", 8081),
        fetch_pozdrav("/pozdrav", 8082)
    ]
    results = await asyncio.gather(*tasks)
    print(results)

if __name__ == "__main__":
    asyncio.run(main())
