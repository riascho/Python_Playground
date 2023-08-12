import itertools

def permutation(digits): # does not take repetitions into account
  count = 0
  for n in itertools.permutations(pin_numbers,digits):
    count +=1
  print("you would need at max",count,"attempts to hack a PIN number")

def repeated(digits): # combinations including repetition
  count = 0
  for n in itertools.product(pin_numbers,repeat=digits):
    count +=1
  print("you would need at max",count,"attempts to hack a PIN number of",digits,"digits.")

pin_numbers = [0,1,2,3,4,5,6,7,8,9]
digit = 4
count = 0

repeated(4)