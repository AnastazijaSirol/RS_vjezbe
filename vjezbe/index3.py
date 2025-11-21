import VremenskaPrognoza
from datetime import datetime, timedelta
import asyncio
import random
import time

objekt = VremenskaPrognoza.VremenskaPrognoza("Pazin", 13, datetime(2003, 10, 2))

objekt.ispis()

async def simuliraj_temp(broj_dana, isCool):
    await asyncio.sleep(0.1)
    return [
        {
            "dan": x,
            "temp_zraka": random.randint(0, 20) if isCool else random.randint(20, 40)
        }
        for x in range(1, broj_dana + 1)
    ]

async def simuliraj_mjesec(lista, grad):
    for dan in lista:
        nova_temp = dan["temp_zraka"]
        novi_datum = grad.datum + timedelta(days=1)

        grad.dnevna_promjena(nova_temp, novi_datum)
        grad.ispis()

async def main():
    hladni_dani = await simuliraj_temp(30, True)

    moj_grad = VremenskaPrognoza.VremenskaPrognoza("Pula", 14, datetime.now())

    await simuliraj_mjesec(hladni_dani, moj_grad)

    '''prva = asyncio.create_task(simuliraj_temp(3, True))
    druga = asyncio.create_task(simuliraj_temp(2, False))
    rez1 = await prva
    rez2 = await druga
    return rez1, rez2'''

    '''prva = await simuliraj_temp(3, True)
    druga = await simuliraj_temp(2, False)
    return prva, druga'''

#t1 = time.perf_counter()
print(asyncio.run(main()))
#t2 = time.perf_counter()

#print(round(t2-t1, 2))

# Bilo je duplo brže konkurentno
# Sekvencijalno - izvršava se jedna do kraja pa druga do kraja
# Konkurentno - dio prvog i drugog poziva izvršava se paralelno