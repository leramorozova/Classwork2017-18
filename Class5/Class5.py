import json
import urllib.request
import re
import os

def example():
    user = "elmiram"  # пользователь, про которого мы хотим что-то узнать
    url = 'https://api.github.com/users/%s/repos' % user
    # по этой ссылке мы будем доставать джейсон, попробуйте вставить ссылку в браузер и посмотреть, что там

    response = urllib.request.urlopen(url)  # посылаем серверу запрос и достаем ответ
    text = response.read().decode('utf-8')  # читаем ответ в строку
    data = json.loads(text) # превращаем джейсон-строку в объекты питона

    print(len(data))  # можно распечатать, сколько у пользователя репозиториев
    for i in data:
        print(i["name"]) # и распечатать названия всех репозиториев


#Часть 1. Про гитхаб.
#Вот, например, несколько (не)случайных юзеров гитхаба: elmiram, nevmenandr, shwars, JelteF, timgraham, arogozhnikov, accommodavid, jasny, bcongdon, whyisjake.
#Вам нужно:
#1) Выбрать какого-то одного пользователя и распечатать список его репозиториев (name) и их описания (description).
#2) На каких языках пишет выбранный пользователь? Распечатать список языков (language) и количество репозиториев, в котором они используются.
#3) У кого из пользователей в списке больше всего репозиториев?
#4) Какой язык самый популярный среди пользователей списка?
#5) У кого из пользователей списка больше всего фолловеров? (фолловеров можно достать по ссылке https://api.github.com/users/username/followers, где вместо username -- имя пользователя)

def task_12():
    user = "nevmenandr"
    url = 'https://api.github.com/users/%s/repos' % user
    response = urllib.request.urlopen(url)
    text = response.read().decode('utf-8')
    data = json.loads(text)
    lang={}
    for el in data:
        print(el["language"])
        print(el["name"], '----', el["description"]) #1
        if el["language"] in lang:
            lang[el["language"]]+= 1
        else:
            lang[el["language"]] = 1
    for key in lang:
        print(key, '----', lang[key]) #2


def task_3():
    repos_num={}
    repos_lang={}
    max_name=''
    max_num=0
    max_name_lang=''
    max_lang=0
    users = ["elmiram", "nevmenandr", "shwars", "JelteF", "timgraham", "arogozhnikov", "jasny", "bcongdon", "whyisjake"]
    for user in users:
        url = 'https://api.github.com/users/%s/repos' % user
        try:
            page = urllib.request.urlopen(url)
            text = page.read().decode('utf-8')
            data = json.loads(text)
            repos_num[user] = len(data)
            for el in data:
                print(el["language"])
                if el["language"] in lang:
                    repos_lang[el["language"]] += 1
                else:
                    repos_lang[el["language"]] = 1
        except:
            print('Error at', url)
    for user in repos_num:
        if repos_num[user]>max_num:
            max_num=repos_num[user]
            max_name=user
        elif repos_num[user]==max_num:
            max_name= max_name +', '+user
    for key in repos_lang:
        if repos_lang[key]>max_lang:
            max_lang=repos_lang[key]
            max_name_lang=key
#    print (max_name)
#    print(max_name_lang)

#task_12()
#task_3()

# Часть 2. Мы же все-таки лингвисты.
# Вот например есть такой json. Нужно прочитать этот файл и записать на его основе XML, как в НКРЯ.

def task_p2():
    file = open('/home/lera/Classwork2017-18/json.txt', 'r', encoding='utf-8')
    text=file.read()
    reg=re.findall('"text":"(.*?)"', text)
    for el in reg:
        need=''.join(reg)
    mass=need.split('\\\\s')
    new_text=''.join(mass)
    new_file = open('/home/lera/Classwork2017-18/json_clean.txt', 'w', encoding='utf-8')
    text=new_file.write(new_text[:-2]) #прлучившийся файл надо скопировать в другое место
#   Если файл для инпута взят из того же места, где был создан, в аутпуте пустой файл
#   Контрится копированием в новую папку инпута
    os.system(r"/home/lera/ms/mystem -i -n -d -e utf-8 --format xml /home/lera/input/json_clean.txt /home/lera/output/json_stem.xml")


task_p2()