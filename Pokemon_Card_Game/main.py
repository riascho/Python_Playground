import json
from urllib.request import urlopen, Request

api_url = "https://pokeapi.co/api/v2/pokemon/"
req = Request(url=api_url,headers={'User-Agent': 'Mozilla/5.0'})
source = urlopen(req).read()

data = json.load(source)

print(data)