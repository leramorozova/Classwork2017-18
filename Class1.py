#1. Скачать главную страницу Яндекс.Погоды и
#   а) распечатать сегодняшнюю температуру и облачность
#   б) распечатать время восхода и заката
#   в) погоду на завтра

import urllib.request
import re

def task_1():
    html_code = urllib.request.Request('https://yandex.ru/pogoda/moscow')
    with urllib.request.urlopen(html_code) as response:
        html_info = response.read().decode('utf-8')
        temp = re.search('<div class="current-weather__thermometer current-weather__thermometer_type_now">(.*?)</div>', html_info)
        cloud = re.search('<span class="current-weather__comment">(.*?)</span>', html_info)
        sunrise = re.search('<span class="current-weather__info-label">(Восход: )</span>(.{,5})', html_info)
        sunset = re.search('<span class="current-weather__info-label current-weather__info-label_type_sunset">(Закат: )</span>(.{,5})', html_info)
        print('Температура в Москве на данный момент: ' + str(temp.group(1)))
        print('Облачность в Москве на данный момент: ' + str(cloud.group(1)))
        print(str(sunrise.group(1)) + str(sunrise.group(2)))
        print(str(sunset.group(1)) + str(sunset.group(2)) + '\n')

        tomorrow=re.search('(.*?)"dayIndex":2(.*?)(Максимальная температура днём)">(.*?)</div>(.*?)(Минимальная температура ночью)">(.*?)</div>', html_info)
        print('Прогноз на завтра:')
        print(str(tomorrow.group(3))+ ' ' + tomorrow.group(4))
        print(str(tomorrow.group(6)) + ' ' + tomorrow.group(7))

#2. Скачать главную страницу waitbutwhy.com. Распечатать заголовки популярных постов (которые в колонке справа
#с надписью Popular Posts) и количество комментариев у каждого из них.

def task_2():
    url = 'https://waitbutwhy.com/'
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    req = urllib.request.Request('https://waitbutwhy.com/', headers = {'User-Agent': user_agent})
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        reg1 = re.search('Popular Posts</a></h5></li>.*?<!-- /tiles -->', html, flags = re.DOTALL)
        populars=reg1.group()
        info=re.findall('<a href=".*?">.*?</a>.*?[0-9]{1,4}</a>', populars, flags = re.DOTALL)
        for el in info:
            reg2=re.search('<h5>.*?<a href=".*?">(.*?)</a>.*?<i class="icon-comments"></i>(.*?)</a>', el, flags = re.DOTALL)
            name=reg2.group(1)
            comments=reg2.group(2)
            print('Название статьи: ', name, '\n', 'Количество комментариев к ней: ', comments)

def main():
    task_1()
    task_2()

main()