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
    jedan = asyncio.create_task(simulate_movement(1, 30))
    dva = asyncio.create_task(simulate_movement(2, 30))
    tri = asyncio.create_task(simulate_movement(3, 30))
    cetri = asyncio.create_task(simulate_movement(4, 30))
    pet = asyncio.create_task(simulate_movement(5, 30))
    
    positions = [jedan, dva, tri, cetri, pet]

    rezultat = await asyncio.gather(*positions)

    '''sve = sum((len(r) for r in rezultat))

    print(sve)'''

    normal = [dio for lista in rezultat for dio in lista]

    prvih_50 = normal[:50]

    pozvani_50 = [update_camera_location(instanca, x, y) for (x, y) in prvih_50]

    await asyncio.gather(*pozvani_50)

    # await update_camera_location(instanca, 5, 5)


async def update_camera_location(instance, x, y):
    instance.update_location(x, y)
    instance.info()

if __name__ == "__main__":
    asyncio.run(main())