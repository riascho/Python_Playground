def test(word):
  letters = list(word)
  if letters == letters[::-1]:
    return True

def palindrome(word):
  if len(word)<=1:
    return True
  if word[0] != word[-1]:
    return False
  return palindrome(word[1:-1]) #recursion

word = input("Enter Word / Sentence to test for palindrome:\n> ").lower().replace(" ","")
print()
if test(word) == True:
  print("Yep! Palindrome")
else:
  print("No palindrome.")
