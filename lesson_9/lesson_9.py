

# def bubble_sort(arr):
#     def swap(i,j):
#         arr[i], arr[j] = arr[j], arr[i]
#     n = len(arr)
#     swapped=True
#
#     x=-1
#     while swapped:
#         swapped=False
#         x+=1
#         for i in range(1,n-x):
#             if arr[i-1]>arr[i]:
#                 swap(i-1,i)
#                 swapped=True
# words={}
# b=5
# def count_words(sentence):
#     words={}
#     for word in sentence.split():
#         words[word]=words.get(word,0)+1
#     return words
#
# def add_const(x,const=100):
#     return x+const
#
# def foo(x,y):
#     y=x//b
#     x*=b
#     return y
#
# def change_list(changed_list, value):
#     changed_list.append(changed_list[0])
#     changed_list[0]==value
#
# def main():
#     sentence="word word word"
#     count_words(sentence)
#
#
#
# if __name__ == '__main__':
#     main()
#     print(f"{b=}")
#     my_list=[1,2,3,4]
#     change_list(my_list,4)
#     print(my_list)
#     change_list(my_list,4)
#     print(my_list)
# import math
# import time
# import pprint
# pprint.pprint (locals())

# with open("my_dir/__init__.py", "w") as f:
#     pass


# import shutil
# import os
#
# source = os.path.join("my_dir", "main_data.py")
# destination = "main_data.py"


# import sys
# print("Current sys.path:")
# for p in sys.path:
#     print("  ", p)
#
#     if 'test' in sys.modules:
#         del sys.modules['test']

# import sys
# # import os
# # import tempfile
# #
# # custom_dir = tempfile.mkdtemp()
# # with open(os.path.join(custom_dir, "test.py"), "w") as f:
# #     f.write("def test():return 'test!'")
# #
# print("test" in sys.modules)