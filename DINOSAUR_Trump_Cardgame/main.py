import random, os, time

deck = {
  "a": {"name":"Tyrannosaurus Rex","size":12, "speed":5,"intelligence":1, "ferocity":9},
  "b": {"name":"Tricerotops","size":7, "speed":3,"intelligence":2, "ferocity":5}, 
  "c": {"name":"Archaeopteryx","size":5, "speed":6,"intelligence":3, "ferocity":4},
  "d": {"name":"Brontosaurus","size":18, "speed":1,"intelligence":2, "ferocity":2},
  "e": {"name":"Velociraptor","size":8, "speed":8,"intelligence":4, "ferocity":6},
  "f": {"name":"Stegosaurus","size":16, "speed":2,"intelligence":2, "ferocity":2},
  "g": {"name":"Spinosaurus","size":15, "speed":4,"intelligence":2, "ferocity":7},
  "h": {"name":"Brachiosaurus","size":20, "speed":1,"intelligence":2, "ferocity":1},
  "i": {"name":"Allosaurus","size":10, "speed":7,"intelligence":1, "ferocity":10},
  "j": {"name":"Dilophosaurus","size":9, "speed":5,"intelligence":4, "ferocity":3}
  }

def interpreter(option):
  if option == 1:
    return "size"
  elif option == 2:
    return "speed"
  elif option == 3:
    return "intelligence"
  elif option == 4:
    return "ferocity"
  else: 
    print("\nNot a valid input!\n\n")
    time.sleep(2)
    os.system("clear")
    return None

while True: 
  time.sleep(4)
  os.system("clear")
  print("DINOSAUR Top Trump Card Game\n\n")
  card_bot = random.choice(list(deck.keys()))
  card_user = random.choice(list(deck.keys()))
  print(f'\t> You drew "{deck[card_user]["name"]}"\n')
  print(f'\t> Bot drew "{deck[card_bot]["name"]}"\n')
  
  option = interpreter(int(input("Which stat do you want to play?\n\n1: Size\n2: Speed\n3: Intelligence\n4: Ferocity\n\n> ")))
  if option is None:
    continue
  if deck[card_bot][option] > deck[card_user][option]:
    print("Bot wins!\n")
    print(f'{deck[card_bot]["name"]}\n{option.capitalize()}: {deck[card_bot][option]}\n')
    print(f'{deck[card_user]["name"]}\n{option.capitalize()}: {deck[card_user][option]}\n')
  elif deck[card_bot][option] < deck[card_user][option]:
    print("You win! :) \n")
    print(f'{deck[card_user]["name"]}\n{option.capitalize()}: {deck[card_user][option]}\n')
    print(f'{deck[card_bot]["name"]}\n{option.capitalize()}: {deck[card_bot][option]}\n')
  else:
    print("It's a Draw!\nTry again!")
    continue