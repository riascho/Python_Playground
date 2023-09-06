import random, string, secrets

def pin_generator(length=4):
  pin=""
  for i in range (length):
    pin += str(secrets.choice(range(10)))
  return pin 

def password_generator(length=8): 
  characters = string.ascii_letters + string.digits + string.punctuation
  while True: 
    password = "".join(secrets.choice(characters) for i in range(length))
    if any(c.isupper() for c in password) and any(c.isdigit() for c in password) and any(c in string.punctuation for c in password):
      break
  return password


with open("password.txt", "w") as file:
  file.write(password_generator(12))
