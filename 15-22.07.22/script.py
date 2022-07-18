import requests


cities = ['Лондон', 'Шереметьево', 'Череповец']
url_template = 'https://wttr.in/{}'
payload = {'nTqm': '',
            'lang': 'ru'
}

for city in range(len(cities)):
    response = requests.get(url_template.format(cities[city]), params=payload)
    print(response.text)
