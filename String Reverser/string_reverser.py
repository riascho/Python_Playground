import stack

string = input("Enter the text you want reversed:\n")
reversed_string = ""
s = stack.Stack()           # stack.Stack = name of the module . class within that module

for char in string:
    s.push(char)

while not s.is_empty():
    reversed_string += "{}".format(s.pop())

print(reversed_string)
