import asyncio
import random

async def provjeri_parnost(broj):
    await asyncio.sleep(2)
    if broj%2==0:
        return f"Broj {broj} je paran"
    else:
        return f"Broj {broj} je neparan"
    
async def main():
    lista = [random.randint(1, 100) for i in range(10)]
    print(lista)

    zadaci = [asyncio.create_task(provjeri_parnost(b)) for b in lista]

    rezultat = await asyncio.gather(*zadaci)

    for r in rezultat:
        print(r)
    
asyncio.run(main())