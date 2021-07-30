from typing import List, NewType


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


# print(rev_string("apple"))
# print(rev_string("1234567890"))


def par_balance_checker(symbol_string):
    """function to check if paranthesis are balanced"""
    new_stack = Stack()
    for symbol in symbol_string:
        if symbol == "(":
            new_stack.push(symbol)
        else:
            if new_stack.is_empty():
                return False
            else:
                if not matches(new_stack.pop(), symbol):
                    return False
    return new_stack.is_empty()


def matches(left_symbol, right_symbol):
    all_lefts = "([{"
    all_rights = ")]}"
    return all_lefts.index(left_symbol) == all_rights.index(right_symbol)


# print(par_balance_checker("(())"))
# print(par_balance_checker("(())))"))
# print(par_balance_checker("{({([][])}())}"))
# print(par_balance_checker("[{()]"))


def divide_by_2(decimal_num):
    """function for decimal-to-binary conversion"""
    rem_stack = Stack()

    while decimal_num > 0:
        rem = decimal_num % 2
        rem_stack.push(rem)
        decimal_num = decimal_num // 2

    bin_string = ""
    while not rem_stack.is_empty():
        bin_string = bin_string + str(rem_stack.pop())

    return bin_string


# print(divide_by_2(42))
# print(divide_by_2(31))


def base_converter(decimal_num, base):
    digits = "0123456789ABCDEF"
    rem_stack = Stack()

    while decimal_num > 0:
        rem = decimal_num % base
        rem_stack.push(rem)
        decimal_num = decimal_num // base

    new_string = ""
    while not rem_stack.is_empty():
        new_string = new_string + digits[rem_stack.pop()]
    return new_string


# print(base_converter(25, 2))
# print(base_converter(25, 8))
# print(base_converter(25, 16))
# print(base_converter(256, 16))
# print(base_converter(26, 26))
