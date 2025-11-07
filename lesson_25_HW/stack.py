#Task 2
from singly_linkedlist import SinglyLinkedList

class Stack:
    def __init__(self):
        self._list = SinglyLinkedList()

    def is_empty(self):
        return self._list.is_empty()

    def push(self, item):
        self._list.add_front(item)

    def pop(self):
        return self._list.remove_front()

    def peek(self):
        return self._list.peek_front()

    def __repr__(self):
        return "Top -> " + repr(self._list)

if __name__ == "__main__":
    stack = Stack()

    stack.push(5)
    stack.push(10)
    stack.push(15)

    print(stack)