import asyncio
import aiohttp
import time

async def fetch_url(sesion: aiohttp.ClientSession, url: str) -> str:
    async with sesion.get(url, timeout=5) as response:
        return await response.text()
    
async def main():
    urls = {
        "https://example.com",
        "https://httpbin.org/get",
        "https://api.github.com",
    }

    async with aiohttp.ClientSession() as sesion:
        content = [fetch_url(sesion, url) for url in urls]
        rezultat = await asyncio.gather(*content)
        for urli, con in zip(urls, rezultat):
            print(len(con), urli)

if __name__ == "__main__":
    t1 = time.perf_counter()
    asyncio.run(main())
    t2 = time.perf_counter()

print(round(t2-t1, 2)) #1.01

'''import requests
import time

def fetch_url(url: str) -> str:
    response = requests.get(url, timeout=5)
    return response.text

def main():
    urls = {
        "https://example.com",
        "https://httpbin.org/get",
        "https://api.github.com",
    }

    for url in urls:
        content = fetch_url(url)
        print({len(content)}, {url})

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()

print(round(t2-t1, 2)) # 2.92'''