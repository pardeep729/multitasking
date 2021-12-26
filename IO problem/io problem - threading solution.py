import requests
import time

import threading
from concurrent.futures import ThreadPoolExecutor

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def download_site(idx, url):
    session = get_session()
    with session.get(url) as response:
        print(f"{idx}: Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites.keys(), sites.values())


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 500
    sites = {idx: s for idx, s in enumerate(sites)}
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")