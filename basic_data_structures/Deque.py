class Deque:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def add_front(self, item):
        self._items.append(item)

    def add_rear(self, item):
        self._items.insert(0, item)

    def remove_front(self):
        return self._items.pop()

    def remove_rear(self):
        return self._items.pop(0)

    def size(self):
        return len(self._items)


def pal_checker(a_string):
    char_deque = Deque()

    for ch in a_string:
        char_deque.add_rear(ch)

    while char_deque.size() > 1:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()

        if first != last:
            return False
    return True


if __name__ == "__main__":
    print(pal_checker("radar"))
    print(pal_checker("lsdkjfskf"))
