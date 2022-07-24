import requests
import os
from urllib.parse import urlparse


token = os.environ['Token']
header = {
    "Authorization": f"Bearer {token}",
}


def shorten_link(token: str, url: str) -> str:
    """Converts a long url to a Bitlink"""
    api_address = 'https://api-ssl.bitly.com/v4/bitlinks'
    data = {
        "long_url": f"{url}",
    }

    try:
        response = requests.post(api_address, headers=header, json=data)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Введена неверная ссылка")
        exit()
    return response.json()["link"]


def count_clicks(token: str, link: str) -> int:
    """Returns the click counts for the specified Bitlink"""
    parts_bitlink = urlparse(link)
    link = parts_bitlink.netloc + parts_bitlink.path
    api_address = f"https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary"
    payload = {
        "unit": "day",
        "units": -1
    }

    try:
        response = requests.get(api_address, params=payload, headers=header)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Не удалось получить информацию, проверьте правильность введенных данных")
    return response.json()["total_clicks"]


def is_bitlink(url: str) -> bool:
    """Verifide url to fit Bitlink"""
    parsed_link = urlparse(url)
    return "bit.ly" in parsed_link


if __name__ == '__main__':
    url = input("Введите ссылку: ")
    if is_bitlink(url):
        print("По вашей ссылке прошли:", count_clicks(token, url), "раз(а)")
    else:
        print("Битлинк:", shorten_link(token, url))



