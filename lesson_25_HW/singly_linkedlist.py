class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove_front(self):
        if self.is_empty():
            raise IndexError("remove from empty list")
        data = self.head.data
        self.head = self.head.next
        return data

    def peek_front(self):
        if self.is_empty():
            raise IndexError("peek from empty list")
        return self.head.data

    def __repr__(self):
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values)