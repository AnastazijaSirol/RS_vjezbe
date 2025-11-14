import asyncio
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

'''async def fetch_data(param):
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

print(f"Vrijeme izvrsavanja: {round(t2 - t1, 2)}")'''

'''def fetch_data(param):
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

print(f"Vrijeme izvrsavanja: {round(t2 - t1, 2)}")'''

'''async def korutina2():
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
