# 11. 
import asyncio

async def pozdrav():
    await asyncio.sleep(1)
    print("Pozdrav")

async def main():
    poz = asyncio.create_task(pozdrav())
    rez = await poz
    return rez

asyncio.run(main())