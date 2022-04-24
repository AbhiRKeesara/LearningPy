class Node:
    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    def get_data(self):
        """Get node data"""
        return self._data

    def set_data(self, node_data):
        """Set node data"""
        self._data = node_data

    data = property(get_data, set_data)

    def get_next(self):
        """Get next node"""
        return self._next

    def set_next(self, node_next):
        """set next node"""
        self._next = node_next

    next = property(get_next, set_next)

    def __str__(self):
        """String"""
        return str(self._data)


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_first(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def add_last(self, item):
        temp = Node(item)
        if self.head is None:
            self.head = temp
            return
        for current_node in self:
            pass
        current_node.next = temp

    def add_after(self, target_node_data, item):
        temp = Node(item)
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data.data:
                temp.next = node.next
                node.next = temp
                return
        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, item):
        temp = Node(item)
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data.data:
            return self.add_first(temp)

        prev_node = self.head

        for node in self:
            if node.data == target_node_data.data:
                prev_node.next = temp
                temp.next = node
                return

            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def size(self):
        count = 0
        for node in self:
            count = count + 1
        return count

    def search(self, item):
        for node in self:
            if node.data == item:
                return True
        return False

    def remove(self, item):
        previous = None
        for node in self:
            if node.data == item:
                break
            previous = node
        if node is None:
            raise ValueError("{} is not in the list".format(item))
        if previous is None:
            self.head = node.next
        else:
            previous.next = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.data)
        nodes.append("None")
        return "".join(str(nodes))

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


if __name__ == "__main__":
    my_list = UnorderedList()
    my_list.add_first(31)
    my_list.add_first(41)
    my_list.add_last(51)
    my_list.add_last(61)
    my_list.add_after(Node(61), 71)
    my_list.add_before(Node(61), 81)
    print(my_list.size())

    print(my_list.search(61))
    print(my_list)
