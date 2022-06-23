import requests

URL = 'https://api.imgflip.com/get_memes'

r = requests.get(url=URL)

print(len(r.json()['data']['memes']))

for x in range(100):
    print(r.json()['data']['memes'][x]['url'])




