# class Node:
#     def __init__(self, data, prev=None, next=None):
#         self.data = data
#         self.prev = prev
#         self.next = next
#
#     def __str__(self):
#         return f"<Node: {self.data}>"
#
# class CustomDeque:
#     def __init__(self, iterable=None):
#         self.head = None
#         self.tail = None
#
#         if iterable is not None:
#             for item in iterable:
#                 self.append(item)
#
#     def is_empty(self):
#         return self.head is None
#
#     def append(self, data):
#         """Add to the right (tail)"""
#         new_node = Node(data)
#         if self.is_empty():
#             self.head = self.tail = new_node
#         else:
#             new_node.prev = self.tail
#             self.tail.next = new_node
#             self.tail = new_node
#
#     def appendleft(self, data):
#         """Add to the left (head)"""
#         new_node = Node(data)
#         if self.is_empty():
#             self.head = self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node
#
#     def pop(self):
#         """Remove from the right (tail)"""
#         if self.is_empty():
#             raise IndexError("pop from an empty deque")
#         data = self.tail.data
#         self.tail = self.tail.prev
#         if self.tail is None:
#             self.head = None
#         else:
#             self.tail.next = None
#         return data
#
#     def popleft(self):
#         """Remove from the left (head)"""
#         if self.is_empty():
#             raise IndexError("popleft from an empty deque")
#         data = self.head.data
#         self.head = self.head.next
#         if self.head is None:
#             self.tail = None
#         else:
#             self.head.prev = None
#         return data
#
#     def __str__(self):
#         nodes = []
#         current = self.head
#         while current:
#             nodes.append(str(current.data))
#             current = current.next
#         return "CustomDeque: [" + " <-> ".join(nodes) + "]"
#
#     def __len__(self):
#         count = 0
#         current = self.head
#         while current:
#             count += 1
#             current = current.next
#         return count
#
#     def __bool__(self):
#         return not self.is_empty()
#
# if __name__ == "__main__":
#     d = CustomDeque()
#     for i in range(3):
#         d.appendleft(1)
#         d.appendleft(2)
#
#     print(d)
#

# stack_1 = [10, 20, 30]
# top_element = stack_1[-1]
# print(top_element)

# word_1=['cat','dog','parrot']
# result=map(lambda x:x[0],word_1)
# print(list(result))
#
# s='hhjyu789k'
# for char in s:print(char, char.isalpha())

# from collections import deque
#
# # Initialize an empty queue
# queue = deque()
#
# # Enqueue elements into the queue
# queue.append("A")  # enqueue 'A'
# queue.append("B")  # enqueue 'B'
# queue.append("C")  # enqueue 'C'
#
# # View the queue
# print("Queue contents:", list(queue))
#
# front = queue.popleft()  # This acts as dequeue()
# print("Dequeued:", front)
# print("Queue after dequeue:", list(queue))
#

# from collections import defaultdict
#
# s = 'mississippi'
# d = defaultdict(int)
#
# for char in s:
#     d[char] += 1
#
# print(d)

#
# class Stack:
#     def __init__(self):
#         self._items = []
#
#     def is_empty(self):
#         return len(self._items) == 0
#
#     def push(self, item):
#         self._items.append(item)
#
#     def pop(self):
#         if not self.is_empty():
#             return self._items.pop()
#         else:
#             raise IndexError("pop from an empty stack")
#
# if __name__ == '__main__':
#     stak_1=Stack()
#
#     input_data=input("Enter some characters: ")
#     for char in input_data:
#         stak_1.push(char)
#
#     print("Reverse order of characters:", end=" ")
#     while not stak_1.is_empty():
#         print(stak_1.pop(), end="")
#     print()
