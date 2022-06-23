import requests
import csv
import json


dataURL = 'https://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=json&tzshift=0'

data = requests.get(url=dataURL)
print(data.json())


with open('jsondata.json', 'w') as f:
    json.dump(data.json(), f, indent=2)
    print("Data successfully transferred")

