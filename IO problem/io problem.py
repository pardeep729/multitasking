# Lots of I/O related calls. Lots of calls to websites. Therefore lots of waiting for responses, so wasted idle time.
# Threading means having multiple trains of thought for the same brain.

import requests
import time

def download_site(idx, url, session):
    with session.get(url) as response:
        print(f"{idx}: Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with requests.Session() as session:
        for idx, url in sites.items():
            download_site(idx, url, session)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 50
    sites = {idx: s for idx, s in enumerate(sites)}
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")