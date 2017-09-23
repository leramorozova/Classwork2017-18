# Придумать любой словарь, например, Страна -> (столица, население) или Имя -> (город проживания, возраст).
# Распечатать словарь, используя форматирование с %.

def percents():
    d={}
    for key in range(3):
        key=input('Enter any name: ')
        d[key]=int(input('Enter his or her age: '))
    row='%s\t\t\t%d'
    for key in d:
        print(row % (key, d[key]))


# Для каждого элемента словаря из задания 1 создать папку. Внутри этой папки создать файл,
# в котором будет записано значение соответствующего элемента в словаре.
# Например, у вас есть в словаре Россия -> (Москва, 7000000). Тогда нужно создать папку "Россия",
# а в ней файл с любым названием, содержащий запись "Москва, 7000000".

import os
import shutil

def file_creator():
    d = {}
    for key in range(1):
        key = input('Enter any country: ')
        d[key] = input('Enter the name of its capital and the quantity of its population: ')
    for key in d:
        os.makedirs(key)
        f = open(key +'.txt', 'w', encoding='utf-8')
        f.write(d[key])
        shutil.move(os.path.abspath('.')+'/'+key +'.txt', key)


# Вспомните адрес сайта своей газеты. =В
# Напишите программу, которая извлекает со страницы газетной статьи метаданные:
    # Название статьи
    # Имя автора (если указано)
    # Дату публикации
    # Категории (если есть)
# Для начала можно скачать html-код какой-то статьи и попробовать вытаскивать информацию из него.
# А потом убедитесь, что программа не падает на разных статьях.

import urllib.request
import re

def download_page(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    return html

def data(html):
    reg_name = re.search('<div class="((clauses-name-id)|(content))">.*?<h(1|2)>(.*?)</h(2|1)>.*?</?div', html, flags=re.DOTALL)
    reg_date=re.search('<div class="(number_current_id)|(news-date)">(<a.*?>)?(.*?)(</a>)?</div>', html, flags=re.DOTALL)
    reg_author = re.search('<div class="clauses_anons"><p>(.*?)</p>', html, flags=re.DOTALL)
    if reg_date!=None:
        date=reg_date.group(4)
    else:
        date='no data'
    if reg_name!=None:
        name=reg_name.group(5)
    else:
        name='no data'
    if reg_author!=None:
        author=reg_author.group(1)
    else:
        author='no data'
    print('Название: '+name+'\n'+'Дата '+ date+'\n'+'Автор: '+author+'\n'+'А категории нет')

data(download_page('test url'))
