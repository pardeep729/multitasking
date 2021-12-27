import requests
import time

import multiprocessing

session = None

def set_global_session():
    global session
    if not session:
        session = requests.Session()

def download_site(site):
    idx = site[0]
    url = site[1]
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{idx}: {name}: Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites.items())


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