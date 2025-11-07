# class Empty(Exception):
#   pass
#
# class Node:
#     def __init__(self, data, next=None):
#         self.data=data
#         self.__next=next
#
#
#     @property
#     def next(self):
#         return self.__next
#
#     @next.setter
#     def next(self, addr):
#         if not isinstance(addr, Node):
#             raise TypeError("next must be a Node")
#         self.__next=addr
#
#
#     def __str__(self):
#         return f"<Node: {self.data}>"
#
#
# class CustomQueue:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#         self.__size=0
#
#     def put(self,data):
#         node=Node(data)
#         if not self.tail:
#             self.head=node
#             self.tail=node
#         else:
#             self.tail.next=node
#             self.tail=node
#
#     def get(self):
#         if self.head:
#             node=self.head
#             data=node.data
#             if self.head is not self.tail:
#                 self.head=node.next
#             else:
#                 self.head=None
#                 self.tail=None
#         else:
#             raise Empty("Queue is empty")
#
#     def empty(self):
#         return self.head is None
#
#     def __str__(self):
#         text_list= []
#         current=self.head
#         while current is not None:  #to check if the same id
#             text_list.append(str(current))
#             current=current.next
#         return "\n".join(text_list)
#         # print(self.tail)
#
#
#
#
#
#
#
# if __name__ == "__main__":
#     # node = Node(10)
#     # node2=Node(20)
#     # node.next = node2
#
#     # print(node)
#     # print(node2)
#     # print(id(node), id(node2), id(node.next))
#
#     c_queue=CustomQueue()
#     for i in range (1,4):
#         c_queue.put(i)
#
#
#     print(c_queue)
#     print(c_queue.get())
#     print(c_queue.get(),c_queue.get())
#
#
#     c_queue.put(10)
#     print(c_queue)



class Node:
    def __init__(self, data, prev=None, next=None):  # , prev=None
        self.data = data
        self.prev = prev
        self.__next = next

    @property
    def next(self):
        return self.__next

    def __str__(self):
        return f"<Node: {self.data}>"

class CustomDeque:
    def __init__(self, iterable=None):
        self.head=None
        self.tail=None
        self.__size=0

        if iterable is not None:
            for item in iterable:
                self.append(item)

    def is_empty(self):
        return self.head is None

    def append(self, data):
        node_1=Node(data)
        if self.is_empty():
            self.head =self.tail=node_1
        else:
            node_1.prev=self.tail
            self.tail.next=node_1
            self.tail=node_1

    def appendleft(self, data):
        node_1=Node(data)
        self.__size+=1
        if self.is_empty():
            self.head =self.tail=node_1
        else:
            node_1.next=self.head
            self.head.prev=node_1
            self.head=node_1


    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty deque")

        removed_data=self.tail.data

        if self.head==self.tail:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.next











