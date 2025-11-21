import asyncio
import time

korisnici = {
    "korisnik1": "lozinka1",
    "korisnik2": "lozinka2",
    "korisnik3": "lozinka3"
}

async def autentifikacija(ime, lozinka, timeout):
    odb = await asyncio.sleep(timeout)
    if odb: 
        raise TimeoutError
    time.sleep(2)
    for _ in korisnici:
        if ime in korisnici and korisnici[ime]==lozinka: 
            return True
        else:
            raise ValueError

async def main():
    a = asyncio.create_task(autentifikacija("korisnik1", "lozinka1", 1))
    b = asyncio.create_task(autentifikacija("korisnik2", "lozinka2", 1))
    c = asyncio.create_task(autentifikacija("korisnik3", "lozinka3", 1))
    #d = asyncio.create_task(autentifikacija("korisnik4", "lozinka4"))
    #e = asyncio.create_task(autentifikacija("korisnik5", "lozinka5"))

    rezultat = await asyncio.gather(a, b, c)

    print(rezultat)

asyncio.run(main())

