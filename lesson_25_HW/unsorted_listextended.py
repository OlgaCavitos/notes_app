#Task 1

from unsorted_list import UnsortedList
from node import Node

class UnsortedListExtended(UnsortedList):

    def append(self, item):
        new_node = Node(item)
        if self.is_empty():
            self._head = new_node
        else:
            current = self._head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)

    def index(self, item):
        current = self._head
        idx = 0
        while current is not None:
            if current.get_data() == item:
                return idx
            current = current.get_next()
            idx += 1
        raise ValueError(f"{item} not found in list")

    def pop(self, pos=-1):
        size = self.size()
        if size == 0:
            raise IndexError("pop from empty list")
        if pos < 0:
            pos += size
        if pos < 0 or pos >= size:
            raise IndexError("pop index out of range")

        current = self._head
        previous = None
        idx = 0
        while idx < pos:
            previous = current
            current = current.get_next()
            idx += 1

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

        return current.get_data()

    def insert(self, pos, item):
        new_node = Node(item)
        if pos <= 0 or self.is_empty():
            new_node.set_next(self._head)
            self._head = new_node
            return

        current = self._head
        previous = None
        idx = 0
        while current is not None and idx < pos:
            previous = current
            current = current.get_next()
            idx += 1

        new_node.set_next(current)
        if previous:
            previous.set_next(new_node)

    def slice(self, start, stop):
        if start < 0 or stop < 0 or start > stop:
            raise ValueError("Invalid slice")

        current = self._head
        idx = 0
        new_list = UnsortedListExtended()

        while current is not None and idx < stop:
            if idx >= start:
                new_list.append(current.get_data())
            current = current.get_next()
            idx += 1

        return new_list


if __name__ == "__main__":
    lst = UnsortedListExtended()
    lst.append(5)
    lst.append(10)
    lst.append(20)
    lst.insert(1, 7)

    print(lst)
    sliced = lst.slice(1, 3)
    print(sliced) 