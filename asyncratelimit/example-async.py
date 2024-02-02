import httpx
import asyncio
from rich import print

async def request_data(client, url):
    resp = await client.get(url)
    return resp.json()


async def main():
    async with httpx.AsyncClient() as client:
        tasks = [request_data(client, "http://localhost:4000/") for _ in urls]
        data = await asyncio.gather(*tasks)
    return data


urls = list(range(1, 1000))
results = asyncio.run(main())
errors = sum(1 for e in results if 'Error' in e.values())
sucesses = sum(1 for e in results if 'Successful' in e.values())
output = {"sucesses": sucesses, "errors": errors}
print(output)
print(results)

