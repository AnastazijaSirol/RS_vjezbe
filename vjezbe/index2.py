import cctv
import asyncio
import random

instanca = cctv.CCTV_frame(1, 10, 20, 30, "Active", "1x", "192.168.1.10")

instanca.info()

async def simulate_movement(sec, frame_rate):
    await asyncio.sleep(sec)
    result = [
        (random.uniform(-100, 100), random.uniform(-100, 100)) for _ in range(1, frame_rate*sec+1)
    ]

    return result

async def main():
    '''result = await simulate_movement(2, 3)
    print(result)'''
    
    positions = [asyncio.create_task(x, 30) for x in range(5)]

    rezultat = await asyncio.gather(*positions)

    '''sve = sum((len(r) for r in rezultat))

    print(sve)'''

    normal = [dio for lista in rezultat for dio in lista]

    prvih_50 = normal[:50]

    #pozvani_50 = [update_camera_location(instanca, x, y) for (x, y) in prvih_50]

    #await asyncio.gather(*pozvani_50)

    udaljenost = [euclidean_distance((0, 0), (x, y)) for (x, y) in prvih_50]

    print(await asyncio.gather(*udaljenost))

    # await update_camera_location(instanca, 5, 5)
import math

async def update_camera_location(instance, x, y):
    instance.update_location(x, y)
    instance.info()

def euclidean_distance(p1, p2):
    (x1, x2)= p1
    (y1, y2) = p2
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return round(dist, 2)

if __name__ == "__main__":
    asyncio.run(main())