import asyncio
import aiohttp


async def fetch_status(session: aiohttp.ClientSession, url: str):
    async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as resp:
        return resp.status


async def main():
    url_list = [
        "https://httpbin.org/get",
        "https://httpbin.org/headers",
        "https://httpbin.org/ip",
    ]

    async with aiohttp.ClientSession() as session:
        task_coros = [fetch_status(session, url) for url in url_list]
        results = await asyncio.gather(*task_coros)

    for url, status in zip(url_list, results):
        print(f"{url:30s} status code: {status}")


if __name__ == "__main__":
    asyncio.run(main())
