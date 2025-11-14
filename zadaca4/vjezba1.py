import asyncio

async def dohvat_brojeva(): 
    await asyncio.sleep(3)
    podaci = [i for i in range (1, 10)]
    print("Podaci dohvaćeni")
    return podaci

async def main():
    rezultat = await dohvat_brojeva()
    return rezultat

print(asyncio.run(main()))