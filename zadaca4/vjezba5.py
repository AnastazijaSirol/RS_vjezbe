import asyncio

rjecnik = [
    {'prezime': "prezime" ,'broj_kartice': 'enkriptirano1', 'CVV': 'enkriptirano1'},
    {'prezime': "prezime1" ,'broj_kartice': 'enkriptirano11', 'CVV': 'enkriptirano1'},
    {'prezime': "prezime11" ,'broj_kartice': 'enkriptirano111', 'CVV': 'enkriptirano111'}
]

async def secure_data(param):
    await asyncio.sleep(3)
    param["broj_kartice"] = hash(param["broj_kartice"])
    param["CVV"] = hash(param["CVV"])
    return rjecnik

async def main():
    zadaci = [asyncio.create_task(secure_data(r)) for r in rjecnik]
    rezultat = await asyncio.gather(*zadaci)
    for r in rezultat:
        print(r)

asyncio.run(main())