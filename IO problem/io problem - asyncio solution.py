# import requests
import time

import asyncio
import aiohttp # Replaces "requests" so can use asyncio functionalty

# Same function defintion, just with async placed in relevant locations
async def download_site(idx, url, session):
    async with session.get(url) as response:
        print(f"{idx}: Read {len(response.content)} from {url}")

# Async defintion, the "requests" Session has been replaced with "aiohttp" Session + some extra code
async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = [] # Keep a list of tasks to be run
        for idx, url in sites.items():
            task = asyncio.ensure_future(download_site(idx, url, session)) # Wrap normal function call in this syntax
            tasks.append(task) # Populate tasks with all tasks to be run
        await asyncio.gather(*tasks, return_exceptions=True) # Asynchronously runs these tasks, unpacking the list of tasks into the method


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 50
    sites = {idx: s for idx, s in enumerate(sites)}
    start_time = time.time()
    asyncio.run(download_all_sites(sites)) # Wrap a normal function call in this syntax
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")