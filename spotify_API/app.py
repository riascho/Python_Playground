
import requests, json, os
from requests.auth import HTTPBasicAuth
from flask import Flask, request

app = Flask(__name__)

client_ID = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']

url = "https://accounts.spotify.com/api/token"
data = {"grant_type":"client_credentials"}
auth = HTTPBasicAuth(client_ID, client_secret)

response = requests.post(url, data=data, auth=auth)
accessToken = response.json()["access_token"]

def check():
  print(response.ok)
  print()
  print(response.json())
  print()
  print(response.status_code)
  print()
  print(accessToken)

#url = "https://api.spotify.com/v1/me/top/"
headers = {'Authorization': f'Bearer {accessToken}'}
#search = f"{select}?time_range={timeframe}_term&limit=10&offset=0'"

#fullURL = 'https://api.spotify.com/v1/search?q=1985&type=track%2Cartist&limit=10'
#fullURL = f"{url}{search}"

#response = requests.get(fullURL, headers=headers)
#data = response.json()
#print(json.dumps(data, indent=1))

#for i in data["tracks"]["items"]:
#  print(i["artists"][0]["name"])
#  print(i["preview_url"])
#  print()


@app.route('/')
def start():
  page = ""
  f = open("index.html", "r")
  page = f.read()
  f.close()
  return page

@app.route('/', methods=["POST"])
def go():
  form = request.form
  year = form["year"]
  page= f"<h1>{year}</h1>"
  fullURL = f'https://api.spotify.com/v1/search?q=year%3A{year}&type=track%2Cartist&limit=10&offset=0'
  response = requests.get(fullURL, headers=headers)
  data = response.json()
  for track in data["tracks"]["items"]:
    artist= track["artists"][0]["name"]
    title = track["name"]
    preview = track["preview_url"]
    page += f'<h2>{artist}</h2>'
    page += f'<h3>{title}</h3>'
    page += f'<audio controls> <source src="{preview}" type="audio/mpeg"> </audio> <hr>'
  return page

app.run(host='0.0.0.0', port=81)