import json
import time
from pathlib import Path
import requests
from urllib.parse import urlparse

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
}
url = "https://5ka.ru/api/v2/special_offers/"


def get_response(url):
    start_url = "https://5ka.ru/api/v2/special_offers/"
    url = url.replace(urlparse(url).netloc, urlparse(start_url).netloc)

    while True:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response
        time.sleep(1)


def parse(url):
    while url:
        response = get_response(url)
        data: dict = response.json()
        url = data.get("next")
        for product in data.get("results", []):
            dir_path = Path(__file__).parent.joinpath(f"{product['id']}.json")
            save_file = dir_path.write_text(json.dumps(data, ensure_ascii=False))


parse(url)

######################################################################################

"""
С  категорией не могу разобраться потому что 5ка.ru нормально не работает ((((((
"""
