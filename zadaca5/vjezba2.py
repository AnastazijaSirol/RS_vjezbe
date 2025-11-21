import asyncio
import time

def spori_zad1(sec: int):
    print("Započinjem")
    time.sleep(sec)
    print("Gotovo")

async def spori_zad(sec: int):
    print("Započinjem")
    await asyncio.sleep(sec)
    print("Gotovo")

t1 = time.perf_counter()
spori_zad1(2)
spori_zad1(3)
t2 = time.perf_counter()

print(round(t2-t1, 2))

'''async def main():
    prvi = spori_zad(2)
    drugi = spori_zad(3)
    await asyncio.gather(prvi, drugi)'''

async def main():
    prvi = asyncio.create_task(spori_zad(2))
    drugi = asyncio.create_task(spori_zad(3))
    rez1 = await prvi
    rez2 = await drugi
    return rez1, rez2
    
t3 = time.perf_counter()
asyncio.run(main())
t4 = time.perf_counter()

# Kod konkurentonog izvšvanja očekujem da će vrijeme biti jednako vremenu izvršavanja funkcije koja se najviše izvršava (u ovom slučaju 3 sec)

print(round(t4-t3, 2))