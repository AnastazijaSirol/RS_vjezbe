import asyncio

async def dohvat_k():
    await asyncio.sleep(3)
    korisnici = [
        {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
        {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
        {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
        {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
    ]
    return korisnici

async def dohvat_p():
    await asyncio.sleep(5)
    proizvodi = [
        {"naziv": "Laptop", "cijena": 7500},
        {"naziv": "Mobitel", "cijena": 3200},
        {"naziv": "Tipkovnica", "cijena": 250}
    ]
    return proizvodi

async def main():
    rezultat = await asyncio.gather(dohvat_k(), dohvat_p())
    korisnici, proizvodi = rezultat
    print(korisnici, proizvodi)
    return rezultat

asyncio.run(main())