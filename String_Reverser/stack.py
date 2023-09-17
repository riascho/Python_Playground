"""
Taken from: 
Python Data Structures - A Game-Based Approach
Stack class
Robin Andrews - https://compucademy.net/
"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        # return len(self.items) == 0       # alternative, not very phytonic
        return not self.items               # returns true when list is not empty (empty lists always render FALSE)

    def push(self, item):
        self.items.append(item)

    def pop(self):                          # remove last item in stack
        return self.items.pop()

    def peek(self):                         # reveals last item in stack
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):                      # turns the object into a string, so the print function will show the information of the object instead of just the object byte data
        return str(self.items)


if __name__ == "__main__":                  # if this file is directly run by Python, this helps to separate out code (put in Stack function) when imported from somewhere else
    s = Stack()                             # s is the instance of the class and calling the constructor object Stack
    print(s)
    print(s.is_empty())
    s.push(3)
    print(s)
    s.push(7)
    s.push(5)
    print(s)
    print(s.pop())
    print(s)
    print(s.peek())
    print(s.size())
