def list_iteration_test(word):
  letters = list(word)
  if letters == letters[::-1]:
    return True
  else:
     return False

def deque_pop_test(word):
    from collections import deque
    palindrome = deque([])
    test = word
    for letter in test:
        palindrome.append(letter)
    for letter in palindrome:
        if palindrome.popleft() == palindrome.pop():
            return "This is a palindrome!"
        else:
            return "Not a palindrome!"

def recursion_test(word):
  if len(word)<=1:
    return True
  if word[0] != word[-1]:
    return False
  return recursion_test(word[1:-1]) #recursion


word = "racecar"
print(list_iteration_test(word))
print(deque_pop_test(word))
print(recursion_test(word))