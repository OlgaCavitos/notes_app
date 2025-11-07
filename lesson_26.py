# #Linera search Algorithm
#
#
# #[x1,x2,x3, ..., xn-2, xn-1, xn] n -bg   element in container
# import timeit
#
# def line_search(container, element):    #O(n)
#     for item in container:
#         if item == element:
#             return True
#     return False
#
#
# #!!! container is sorted
#
# def binary_search(container, element):    #O(log2 n)
#     idx_start, idx_end=0, len(container)-1
#     found=False
#     while idx_start<=idx_end and not found:
#         idx_middle = (idx_start + idx_end) // 2
#         if container[idx_middle]==element:
#             return True
#         elif container[idx_middle]>element:
#             idx_start=idx_middle + 1
#         else:
#             idx_end=idx_middle - 1
#     return found
#
#
# if __name__ == '__main__':
#     test_list = [i for i in range(-20,100,3)]
#
#     line_search_time = timeit.timeit(
#          stmt="line_search(test_list, 50)",
#          number=100,
#          setup="from __main__ import line_search, test_list")
#
#     print(line_search_time, line_search(test_list, 100))
#
#     binary_search_time = timeit.timeit(stmt="line_search(test_list, 50)",
#          number=100,
#          setup="from __main__ import line_search, test_list")
#     print(line_search_time, line_search(test_list, 100))
#
#
#
# class HasTable:
#     def __init__(self, init_size=8):
#         self.size = init_size
#         self._resize_container
#
#     def __resize_container(self):
#         self.map=[None]*self.size
#         self.order=[]
#
#     def _hash(self, key):
#         return hash(key)%self.size
#
#     def _resize(self):
#         self.size*=2
#         copy_map=self.map.copy()
#         self.__resize_container()
#         for item in copy_map:
#
#
#     def _probe(self, pos):
#         for i in range(pos +1,self.size+pos):
#             i=i % self.size
#             if self.map[i] is None:
#                 return i
#         return None
#
#
#     def add(self, key, value):
#         pos=self._hash(key)
#         if self.map[pos]is None:
#             self.map[pos]=key,value
#             self.order.append(pos)
#         else:
#             new_pos=self._probe(pos)
#             if new_pos is not None:
#                 self.map[new_pos]=key,value
#                 self.order.append(pos)
#             else:
#                 self._resize()
#                 self.add(key, value)
#
#
#     def get(self, key):
#         pos=self._hash(key)
#         if self.map[pos] is None and self.map[pos][0]==key:
#             return self.map[pos][1]
#         else:
#             for i in range(pos +1,self.size+pos):
#                 i =i % self.size
#                 if self.map[i] is None:
#                     return None
#                 if self.map[i][0]==key:
#                     return self.map[i][1]
#
#     #def delete
#     # from self.order
#
#
#     # def __len__(self):
#     #     return None
#     #
#     # def __contains__(self,item):
#     #     return ...
#     #
#     #
#     # def __str__(self):
#     #     return str(self.map)
#
#
#
