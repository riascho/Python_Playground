import random, os, time

print("*** HANGMAN GAME***")
print()
print("I got a word for you to guess!")
print()

list_of_words = ["apple", "pineapple", "pear", "accent", "evil", "genius", "downtown","galaxy","power", "hour"]

word = random.choice(list_of_words).lower()
list_of_letters_used = []
vowels = ["a","i","o","u","e"]
count = 0
count_vowel = 0

for i in word:
  if i in vowels:
    count_vowel += 1

length=len(word)
print("There are ",length,"letters in this word.")
print()
print("Hint: Vowels:", count_vowel)

def ascii():
  if count == 1:
    print("""  
  
     
      
      
      |
      |
=========
""")
    print(f'Only {7-count} lives left!')
  elif count == 2:
    print("""  
  
     
      
      |
      |
      |
=========
""")
    print(f'Only {7-count} lives left!')
  elif count == 3:
    print("""  
  
      
      |
      |
      |
      |
=========
""")
    print(f'Only {7-count} lives left!')
  elif count == 4:
    print("""  
   
      |
      |
      |
      |
      |
=========
""")
    print(f'Only {7-count} lives left!')
  elif count == 5:
    print("""  
  +---+
      |
      |
      |
      |
      |
=========
""")
    print(f'Only {7-count} lives left!')
  elif count == 6:
    print("""  
  +---+
  |   |
      |
      |
      |
      |
=========
""")
    print(f'Only {7-count} lives left!')
  elif count == 7:
    print("""  
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========

GAME OVER! :(
""")



while True:
  time.sleep(3)
  os.system("clear")
  guess = input("\n\ntype letter > ").strip().lower()

  if guess in list_of_letters_used:
    print('You already had that one!')
    continue

  list_of_letters_used.append(guess)

  win = True
  for i in word:
    if i in list_of_letters_used:
      print(i, end=" ")
    else:
      print("_", end=" ")
      win = False

  if guess not in word:
    print(f"\n\n{guess} is not in the word!")
    count += 1
  elif guess in word:
    print("\n\nYou found one!")

  ascii()
  if win:
    print("You've won! :)")
    break
  if count == 7:
    break
