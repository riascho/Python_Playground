import random

choice=int(input("""Do you want to create a PIN or password? 
Enter '1' for PIN and '2' for password
> """))

def pin_generator(digits):
  print("PIN Generator")
  pin=""
  for i in range (digits):
    pin += str(random.randint(0,9))
  return pin 

def password_generator(length):
  print("PASSWORD Generator")
  list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","#","_","-","*","&","?","!"]  
  password=""
  for i in range(length):
    password += random.choice(list)
  return password

if choice == 1:
    digits=int(input("How many digits do you need? "))
    print("PIN: ",pin_generator(digits))
elif choice == 2:
    length=int(input("How long does your password need to be? Number of characters: "))
    print("PASSWORD: ",password_generator(length))