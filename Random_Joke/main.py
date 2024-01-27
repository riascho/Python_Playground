import requests, json, os
from replit import db

def joke():  
  result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"}) 
  jk = result.json()["joke"]
  id = result.json()["id"]
  print(jk)
  return jk, id

def save(jk, id):
  db[id] = jk
  print("Joke saved")
  return

def view():
  for entry in db.values():
    print(f"{entry}\n\n")

def menu():
  print("The Joke's on You!\n")
  select = input("Generate random Joke or view Joke-Database?\n1: Random Joke\n2:View Jokes\n")
  if select == "1":
    jk=""
    id=""
    joke()
    store = input("Save this Joke?\nYes/No:\t").lower()
    if store[0] == "y":
      save(jk,id)
  if select == "2":
    view()
  select = input("press enter when done")
  return
    
while True:
  menu()
  os.system("clear")