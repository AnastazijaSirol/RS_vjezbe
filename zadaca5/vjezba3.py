import asyncio
import aiohttp

async def get_cat(sesion: aiohttp.ClientSession):
    async with sesion.get("https://catfact.ninja/fact") as rezultat:
        macke = await rezultat.json()
    return macke

async def main():
    async with aiohttp.ClientSession() as sesion: 
        lista = [asyncio.create_task(get_cat(sesion)) for _ in range(20)]
        rezultat = await asyncio.gather(*lista)
        print(rezultat)
        filtrirano = await filter_cat(rezultat)
        print(f"Filtrirano: {filtrirano}")

async def filter_cat(macke):
    nova_lista = [macka["fact"] for macka in macke if "cat" in macka["fact"].lower() or "cats" in macka["fact"].lower()]
    return nova_lista

asyncio.run(main())