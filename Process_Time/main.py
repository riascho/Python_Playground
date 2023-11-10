# shows difference in performance time when iterating

import time
start_time = time.time()

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

print("\nSimple Loop:")
for age in ages: 
  if age >= 21:
    print(age)
print("--- %s seconds ---" % (time.time() - start_time))

print("\nLoop with continue:")
for age in ages: 
  if age < 21:
    continue
  print(age)
print("--- %s seconds ---" % (time.time() - start_time))

print("\nList Comperehension:")
print([age for age in ages if age >= 21])
print("--- %s seconds ---" % (time.time() - start_time))