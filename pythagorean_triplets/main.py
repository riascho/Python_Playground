# Write a function that returns whether a list of numbers contains Pythagorean Triplets. 

# - What are Pythagorean Triplets? = a2 + b2 = c2
# - Should we return boolean or specific numbers? 
# - Should we consider negative numbers? 
# - Should we consider lists with less than 3 or more than 3 numbers? 
# - Which order are these numbers assigned in terms of their variable? 

# Possible Inputs/ Edge Cases: 

# Happy Path: [3,4,5,] => true
# Sad Path: [12,3,2] => false
# Edge Cases: [4] || [-3,4,5]

# Outline of how to approach this

# First check the length of the input, if it matches 3
# Then destructure the lists into the Pythagorean variables a,b and c
# Write if logic to compare if the mathematical equal a2 + b2 equals c2 (the squaring could also be done in a previous separate step)
# return true if that's the case, else false


def pythagorean_triplets(numbers):
    if len(numbers) < 3 or len(numbers)>3:
        return False
    else:
        a,b,c = numbers
    if a**2 + b**2 == c**2:
        return True
    else:
        return False
    
print(pythagorean_triplets([3,4,5]))
print(pythagorean_triplets([12,3,1,7]))
print(pythagorean_triplets([4]))
print(pythagorean_triplets([-3,4,5]))


def pythagorean_triplets2(numbers):
    if len(numbers) < 3:
        return False
    # loops don't go backward when end is reached, so have to account for that:
    numbers.sort()
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if i != j:
                for k in range(j+1,len(numbers)):
                    if k != i and k != j:
                        a,b,c = numbers[i],numbers[j],numbers[k]
                        if a**2 + b**2 == c**2:
                            return True
    return False

print('Other approach:')
print(pythagorean_triplets2([5,4,3]))
print(pythagorean_triplets2([12,3,1,7]))
print(pythagorean_triplets2([4]))
print(pythagorean_triplets2([-3,4,5]))