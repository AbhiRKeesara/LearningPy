class Stack:
    """Stack implementation as a list"""

    def __init__(self):
        """Create new stack"""
        self._items = []

    def is_empty(self):
        """Check if the stack is empty- https://www.geeksforgeeks.org/bool-in-python/"""
        return not bool(self._items)

    def push(self, item):
        """Add an item to the stack"""
        self._items.append(item)

    def pop(self):
        """Remove an item from the stack"""
        return self._items.pop()

    def peek(self):
        """Get the value of the top item in the stack"""
        return self._items[-1]

    def size(self):
        """Get the number of items in the stack"""
        return len(self._items)


s = Stack()

# print(s.is_empty())
# s.push(4)
# s.push("dog")
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.is_empty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())


def rev_string(my_str):
    myStack = Stack()
    rev_str = ""
    for ch in my_str:
        myStack.push(ch)
    while not myStack.is_empty():
        rev_str = rev_str + myStack.pop()
    return rev_str


print(rev_string("apple"))
print(rev_string("1234567890"))
