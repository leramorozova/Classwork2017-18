import urllib.request as req
import re

html_code = req.Request('https://yandex.ru/pogoda/moscow')
with req.urlopen(html_code) as response:
    html_info = response.read().decode('utf-8')
    temp = re.search('<div class="current-weather__thermometer current-weather__thermometer_type_now">(.*?)</div>',
                     html_info)
    print('Температура в Москве на данный момент: ' + str(temp.group(1)))
