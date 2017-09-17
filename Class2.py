# example, выкачиваем много страниц

import urllib.request

def download_page(pageUrl):
    try:
        page = urllib.request.urlopen(pageUrl)
        print(page.geturl()) #итоговый url после переадресации
        text = page.read().decode('ISO-8859-1')
    except:
        print('Error at', pageUrl)
        return
    # do something with the downloaded text

commonUrl = 'http://www.forumishqiptar.com/threads/'
for i in range(160400, 160425):
    pageUrl = commonUrl + str(i)
    download_page(pageUrl)

___________________________________________________________________________________________

# Скачать код страницы, найти ссылку на следующий/предыдущий пост,
# перейти по ней и скачать следующую страницу. И так все - краулер

import re

# на входе ссылка на страницу
# на выходе код страницы + сохраненный файл с ним (имя - номер страницы)

def download_file(url):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    req = urllib.request.Request(url, headers={'User-Agent': user_agent})
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('ISO-8859-1')
    file_name = url[38:44] + '.txt'
    page_code = open(file_name, 'w', encoding='utf-8')
    text = page_code.write(html)
    return html

# по выполнении данного цикла на выходе ссылка на след страницу
# на входе код страницы

def search_link(html):
    reg = re.search('<!-- next / previous.*?<a href="(.*?)">.*?</a>.*?links -->', html, flags = re.DOTALL)
    next_link = 'http://www.forumishqiptar.com/' + reg.group(1)
    return next_link

# цикл скачивает по одной ссылке и переходит по следующей
# это долго, много файлов

new_link = search_link(download_file('http://www.forumishqiptar.com/threads/162496-Ndihm-per-Windows-7'))
while new_link!= None:
    next_page=search_link(download_file(new_link))
    new_link=next_page
else:
    break
print('Done')
