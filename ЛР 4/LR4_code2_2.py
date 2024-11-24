"""Задание 2 комплект 2"""

import requests
from bs4 import BeautifulSoup

def get(city):

    """Функция парсинга погоды, которой передается название города. Затем формируется URL и происходит запрос.
    При успешном запросе, происходит парсинг и извлечение текстовой информации.
    """

    url = f'https://wttr.in/{city}?format=4'
    r = requests.get(url)

    if r.ok:
        s = BeautifulSoup(r.text, 'html.parser')
        weather_info = s.get_text()

        return weather_info.strip()
    else:
        return None

weather_info = get('Санкт-Петербург')
if weather_info:
    print(f'Погода в {weather_info}')
else:
    print(f'Ошибка')