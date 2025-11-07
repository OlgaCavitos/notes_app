from Node import Node
from time import time


class ClosedList:
    def __init__(self, iterable=None):
        self._head = None
        self._size = 0
        if iterable:
            self._fill_from_iterabe(iterable)

    def _fill_from_iterabe(self, iterable):
        if hasattr(iterable, '__iter__') or hasattr(iterable, '__getitem__'):
            self._add_head(iterable[0])
            print(iterable[-1:0:-1])
            for element in iterable[-1:0:-1]:
                self.add(element)
        else:
            print("Object is not iterable")

    def is_empty(self):
        return self._head is None

    def _add_head(self, data):
        temp = Node(data)
        self._head = temp
        self._head.set_next(temp)
        self._size += 1

    def add(self, data):
        temp = Node(data)
        temp.set_next(self._head.get_next())
        self._head.set_next(temp)
        self._size += 1

    def pop_next(self, node):
        next_node = node.get_next()
        node.set_next(next_node.get_next())
        self._size -= 1
        return next_node.get_data()

    def _remove_next(self, current, n_th):
        curr = current
        for _ in range(n_th-1):
            curr = curr.get_next()
        return self.pop_next(curr), curr

    def remove_every(self, n_th):
        current = self._head
        if self._size > 1:
            removed_data, current = self._remove_next(current, n_th-1)
            while self._size > 1:
                removed_data, current = self._remove_next(current, n_th)
        return current.get_data()



    def __str__(self):
        header = f"<{self.__class__.__name__}> "
        result_list = []
        current = self._head
        for _ in range(self._size):
            result_list.append(str(current.get_data()))
            current = current.get_next()
        return header + ' '.join(result_list)


def rem_every(iterable, k):
    while len(iterable) > 1:
        for _ in range(k-1):
            iterable.append(iterable.pop(0))
        iterable.pop(0)


if __name__ == '__main__':
    lst = [i for i in range(1, 100001)]
    c_list = ClosedList(lst)
    # print(c_list)
    start = time()
    released = c_list.remove_every(3)
    print(released, time()-start)

    # lst = [i for i in range(1, 1100)]
    start = time()
    rem_every(lst, 3)
    print(lst[0], time()-start)
