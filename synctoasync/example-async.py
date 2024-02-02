import httpx
import asyncio

async def request_data(client, url):
    resp = await client.get(url)
    return resp.json()['name']


async def main():
    async with httpx.AsyncClient() as client:
        tasks = [
            request_data(
                client, f"https://rickandmortyapi.com/api/character/{i}"
            )
            for i in range(1, 50)
        ]
        characters = await asyncio.gather(*tasks)
        for c in characters:
            print(c)


asyncio.run(main())

