import requests
import sys
import os
from urllib.parse import urlparse


def shorten_link(token: str, url: str) -> str:
    """Converts a long url to a Bitlink"""
    api_address = 'https://api-ssl.bitly.com/v4/bitlinks'
    header = {
        "Authorization": f"Bearer {token}",
    } 
    data = {
        "long_url": url,
    }
    response = requests.post(api_address, headers=header, json=data)
    response.raise_for_status()
    return response.json()["link"]


def count_clicks(token: str, link: str) -> int:
    """Returns the click counts for the specified Bitlink"""
    parsed_link = urlparse(link)
    netloc, path = parsed_link.netloc, parsed_link.path
    api_address = f"https://api-ssl.bitly.com/v4/bitlinks/{netloc}{path}/clicks/summary"
    header = {
            "Authorization": f"Bearer {token}",
    }
    payload = {
        "unit": "day",
        "units": -1
    }
    response = requests.get(api_address, params=payload, headers=header)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(token: str, url: str) -> bool:
    """Verifide url to fit Bitlink"""
    parsed_link = urlparse(url)
    netloc, path = parsed_link.netloc, parsed_link.path
    api_address = f"https://api-ssl.bitly.com/v4/bitlinks/{netloc}{path}"
    header = {
        "Authorization": f"Bearer {token}",
    }
    response = requests.get(api_address, headers=header)
    return response.ok


def main():
    token = os.environ['BITLY_TOKEN']
    url = sys.argv[1]
    try:
        if is_bitlink(token, url):
            print("По вашей ссылке прошли:", count_clicks(token, url), "раз(а)")
        else:
            print("Битлинк:", shorten_link(token, url))
    except requests.exceptions.HTTPError:
        print("Не удалось получить информацию, проверьте правильность введенных данных")


if __name__ == '__main__':
    main()

