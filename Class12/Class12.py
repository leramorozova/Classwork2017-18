import urllib.request
import json

req = urllib.request.Request('https://api.vk.com/method/wall.get?owner_id=1&count=2&v=5.74&access_token=8423c2448423c2448423c244d08441f2a1884238423c244dee1644d9e90529494134bf8')
response = urllib.request.urlopen(req) # да, так тоже можно, не обязательно делать это с with, как в примере выше
result = response.read().decode('utf-8')

data = json.loads(result)

# print(data['response']['items'][1]['text'])  # индекс - номер поста

# print(data['response']['items'][0]['copy_history'][0]['text'])  # индекс - номер репоста

offsets = [0, 1000, 2000, 3000, 4000]
users = set()
for off in offsets:
    req = urllib.request.Request('https://api.vk.com/method/groups.getMembers?group_id=dormitory8hse&v=5.23&offset=' + str(off))
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    data = json.loads(result)
    users = users | set(data['response']['items'])
    print(len(users))
print(data)
print(len(users))


