import random, string

def pin_generator(length):
  pin=""
  for i in range (length):
    pin += str(random.randint(0,9))
  return pin 

def password_generator(length): 
  password=[]
  if length >= 4:
    password.append(string.ascii_uppercase[random.randrange(26)])
    password.append(string.digits[random.randrange(9)])
    for i in range(length-2):
      password.append(random.choice(list))
  else:
    return "Password needs to be at least 4 characters long!"  
  random.shuffle(password)
  password = "".join(password)
  return password

list = []
for letter in string.ascii_letters:
  list.append(letter)
for number in string.digits:
  list.append(number)
for symbol in string.punctuation:
  list.append(symbol)

length = 8
with open("password.txt", "w") as file:
  file.write(password_generator(length))
