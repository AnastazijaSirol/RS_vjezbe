import asyncio

baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

async def autorizacija(param, lozinka):
    await asyncio.sleep(2)
    for l in baza_lozinka:
        if param["korisnicko_ime"] == l["korisnicko_ime"]:
            if l["lozinka"] == lozinka:
                return f"Korisnik: {param["korisnicko_ime"]} Autorizacija uspješna"
            else:
                return f"Korisnik: {param["korisnicko_ime"]} Autorizacija neuspješna"

async def autentifikacija(param, lozinka):
    await asyncio.sleep(3)
    for k in baza_korisnika:
        if k["korisnicko_ime"] == param["korisnicko_ime"] and k["email"] == param["email"]:
            return await autorizacija(k, lozinka)
        return f"Korisnik {param} nije pronađen"
    
async def main():
    rezultat = await autentifikacija(baza_korisnika[0], "lozinka1234")
    return rezultat

print(asyncio.run(main()))