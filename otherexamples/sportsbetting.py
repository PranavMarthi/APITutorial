import requests

url = "https://odds.p.rapidapi.com/v4/sports/upcoming/odds"

querystring = {"regions":"us","oddsFormat":"decimal","markets":"h2h,spreads","dateFormat":"iso"}

headers = {
	"X-RapidAPI-Key": "f737d0bfa3msheadd09b73c3e7e5p180d5djsn5b17383235d5",
	"X-RapidAPI-Host": "odds.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)