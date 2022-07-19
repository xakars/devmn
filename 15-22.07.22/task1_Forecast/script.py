import requests

cities = ['Лондон', 'Шереметьево', 'Череповец']
url_template = 'https://wttr.in/{}'
payload = {
    'nTqm': '',
    'lang': 'ru'
}

for city_name, city in enumerate(cities):
    response = requests.get(url_template.format(cities[city_name]), params=payload)
    response.raise_for_status()
    print(response.text)
