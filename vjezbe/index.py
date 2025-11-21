import asyncio
import requests
import aiohttp
import time

# curl.exe --version
# curl -X GET http://www.google.com
# curl -X POST http://www.google.com -d '{"ime": "Bo", "prezime": "Boo"}'

'''rez = requests.get("http://catfact.ninja/fact")

lista = []

t1 = time.perf_counter()
for i in range(30):
    rez = requests.get("http://catfact.ninja/fact")
    lista.append(rez.json()["fact"])
t2 = time.perf_counter()
print(round(t2-t1, 2))'''

async def cat(sesion: aiohttp.ClientSession):
    # async with aiohttp.ClientSession() as sesija:
    response = await sesion.get("http://catfact.ninja/fact")
    podataka = await response.json()
    return podataka

# context manager input/output operacije
async def main():
    async with aiohttp.ClientSession() as sesion:   
        lista = [asyncio.create_task(cat(sesion)) for i in range(30)]

        rezultati = await asyncio.gather(*lista)

        '''rezultati = []
        for t in lista:
            rezultat = await t
            rezultati.append(rezultat)'''
        print(rezultati)
    '''#rezultat = await cat()
    for i in range(10):
        res = await cat()
    print("Gotova korutina")'''

asyncio.run(main())

'''async def autent(): #
    asyncio.sleep(5)
    raise Exception

async def timer(sec: int):
    print(f"Loop: {sec}")
    await asyncio.sleep(sec)
    return f"Rezultat timera: {sec}"

async def main():
    rez = timer(1) # event loop: scheulde and run
    rez1 = timer(2)
    rez2 = timer(3)

    lista = [timer(n) for n in range(1, 6)]

    task = asyncio.create_task(rez) #schedule
    task1 = asyncio.create_task(rez1)
    task2 = asyncio.create_task(rez2)

    rezultat = await asyncio.gather(*lista, autent()) # schedule and run and gather results
    print(rezultat)
    rezultat = await task # event loop se gasi
    print(rezultat)

asyncio.run(main())'''

'''import asyncio
import time

async def fetch_data(param):
    print(f"Delan {param}")
    await asyncio.sleep(param)
    print("Zavrsavam...")
    return f"{param}"

async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    rezultat = await task2
    rezultat1 = await task1
    print("Završavam main...")
    return rezultat, rezultat1

t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()

print(f"Vrijeme izvrsavanja: {round(t2 - t1, 2)}")

async def fetch_data(param):
    print(f"Delan {param}")
    await asyncio.sleep(param)
    print("Zavrsavam...")
    return f"{param}"

async def main():
    rezultat = await fetch_data(1)
    rezultat1 = await fetch_data(2)
    print("Završavam main...")
    return rezultat, rezultat1

t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()

print(f"Vrijeme izvrsavanja: {round(t2 - t1, 2)}")

def fetch_data(param):
    print(f"Delan {param}")
    time.sleep(param)
    print("Zavrsavam...")
    return f"{param}"

def main():
    rezultat =  fetch_data(1)
    rezultat1 = fetch_data(2)
    print("Završavam main...")
    return rezultat, rezultat1

t1 = time.perf_counter()
main()
t2 = time.perf_counter()

print(f"Vrijeme izvrsavanja: {round(t2 - t1, 2)}")

async def korutina2():
    print("nesto")
    print(asyncio.get_event_loop())
    await asyncio.sleep(3)
    print("nesto drugo")
    return "nesto trece"

asyncio.run(korutina2())

async def korutina(param: int):
    print(f"Pozvana {param}")
    return param

print(type(korutina(1))) # corutine object

async def main():
    print("Pozvana korutina main...")
    await korutina(1)

asyncio.run(main())'''
