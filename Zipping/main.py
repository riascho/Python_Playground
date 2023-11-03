# very simple list zipping # 

list1 = [1,2,3,4,5,6,7]
list2= ["a","b","c","d","e","f","g"]
combo = list(zip(list1, list2))
print(combo)

new_list = [[str(num), letter] for num, letter in combo]
print(new_list)

new_list2 = [str(num) + letter.upper() for num, letter in combo]
print(new_list2)