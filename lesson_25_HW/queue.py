#Task 3
from singly_linkedlist import SinglyLinkedList

class Queue:
    def __init__(self):
        self._list = SinglyLinkedList()

    def is_empty(self):
        return self._list.is_empty()

    def enqueue(self, item):
        self._list.add_front(item)

    def dequeue(self):
        if self._list.is_empty():
            raise IndexError("dequeue from empty queue")

        current = self._list.head
        previous = None

        while current.next is not None:
            previous = current
            current = current.next

        if previous is None:
            data = self._list.head.data
            self._list.head = None
        else:
            data = current.data
            previous.next = None
        return data

    def peek(self):
        if self._list.is_empty():
            raise IndexError("peek from empty queue")

        current = self._list.head
        while current.next is not None:
            current = current.next
        return current.data

    def __repr__(self):
        return "Front -> " + repr(self._list)

if __name__ == "__main__":
    q = Queue()
    q.enqueue("X")
    q.enqueue("Y")
    q.enqueue("Z")
    print(q)