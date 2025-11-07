import random


# def bubble_sort(array):
#     for pass_num in range(len(array) - 1,0,-1):
#         for i in range(pass_num):
#             if array[i] > array[i+1]:
#                array[i],array[i+1]=array[i+1],array[i]
#
#
#
# def bubble_sort_down(array):
#     for pass_num in range(1,len(array)):
#         for i in range(len(array) -1, pass_num-1,-1):
#             if array[i] < array[i-1]:
#                 array[i],array[i-1]=array[i-1],array[i]
#
#
#
#
# def selection_sort(array):
#     for fill_slot in range(len(array) - 1, 0, -1):
#         position_max = 0
#         for location in range(1, fill_slot + 1):
#             if array[location] > array[position_max]:
#                 position_max = location
#
#         # temp = array[fill_slot]
#         # array[fill_slot] = array[position_max]
#         # array[position_max] = temp
#         array[fill_slot],array[position_max] = array[position_max],array[fill_slot]
#
#
# def selection_sort_down(array):
#     for fill_slot in range(0,len(array) - 1):
#         position_min = fill_slot
#         for location in range(fill_slot + 1,len(array)):
#             if array[location] < array[position_min]:
#                 position_min = location
#         if fill_slot != position_min:
#             array[fill_slot],array[position_min] = array[position_min],array[fill_slot]
#
#
#
#
# if __name__ == "__main__":
#     test_list = [random.randint(1, 100) for _ in range(23)]
#     for func in (bubble_sort, bubble_sort_down, selection_sort_down):
#         copy_test_list = test_list[:]
#         func(copy_test_list)
#         print(copy_test_list)
#         # print(selection_sort_down())
#

def _merge_arrays(array, left_half, right_half):
    i, j, k = 0, 0, 0


    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            array[k] = left_half[i]
            i = i + 1
        else:
            array[k] = right_half[j]
            j = j + 1
        k = k + 1

    while i < len(left_half):
        array[k] = left_half[i]
        i = i + 1
        k = k + 1

    while j < len(right_half):
        array[k] = right_half[j]
        j = j + 1
        k = k + 1

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        _merge_arrays(array, left_half, right_half)


if __name__ == "__main__":
    test_list = [random.randint(1, 100) for _ in range(23)]
    for func in (merge_sort):
        copy_test_list = test_list[:]
        func(copy_test_list)
        print(copy_test_list)
        print(func.__name__)
        # print(selection_sort_down())