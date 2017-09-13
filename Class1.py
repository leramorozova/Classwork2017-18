import urllib.request
import re

req = urllib.request.Request('https://yandex.ru/pogoda/moscow')
with urllib.request.urlopen(req) as response:
   html = response.read().decode('utf-8')

page=html.split('><')
for line in page:
    reg_td_w=re.compile('current\-weather.+', flags= re.DOTALL)
    reg=reg_td_w.findall(page)
    for el in reg: