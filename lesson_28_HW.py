#Task 1
import random
import time

def bubble_sort_two_sides(array):
    def swap(i, j):
        array[i], array[j] = array[j], array[i]

    n = len(array)
    start = 0
    end = n - 1
    swaps = 0
    passes = 0
    swapped = True

    while True:
        swapped=False

        for i in range(start, end):
            if array[i] > array[i+1]:
                swap(i,i+1)
                swaps+=1
                swapped = True
        passes += 1
        if not swapped:
            break

        swapped=False
        end-=1

        for i in range(end, start,-1):
            if array[i-1] > array[i]:
                swap(i,i-1)
                swaps+=1
                swapped = True
        passes += 1
        start+=1
    return passes, swaps

#Task2

def merge_sort_without_slice(array, start, end):
    if start >= end:
        return

    mid = (start + end) // 2
    merge_sort_without_slice(array, start, mid)
    merge_sort_without_slice(array, mid + 1, end)
    merge(array, start, mid, end)

def merge(array, start, mid, end):
    left=[]
    right=[]

    for i in range(start, mid+1):
        left.append(array[i])
    for i in range(mid + 1, end+1):
        right.append(array[i])

    i=j=0
    k=start

    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            array[k]=left[i]
            i+=1
        else:
            array[k]=right[j]
            j+=1
        k+=1

    while i<len(left):
        array[k]=left[i]
        i+=1
        k+=1

    while j<len(right):
        array[k]=right[j]
        j+=1
        k+=1


#Task 3

def quick_sort(array, limit):
    quick_sort_helper(array, 0, len(array) - 1, limit)

def quick_sort_helper(array, low, high, limit):
    while low < high:
        if high - low < limit:
            insertion_sort(array, low, high)
            break
        else:
            pivot_index = _partition(array, low, high)
            if pivot_index - low < high - pivot_index:
                quick_sort_helper(array, low, pivot_index, limit)
                low = pivot_index + 1
            else:
                quick_sort_helper(array, pivot_index + 1, high, limit)
                high = pivot_index

def _partition(array, low, high):
    pivot = array[(low + high) // 2]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while array[i] < pivot:
            i += 1

        j -= 1
        while array[j] > pivot:
            j -= 1

        if i >= j:
            return j

        array[i], array[j] = array[j], array[i]

def insertion_sort(array, low, high):
    for i in range(low + 1, high + 1):
        key = array[i]
        j = i - 1
        while j >= low and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
            array[j + 1] = key



if __name__ == "__main__":
    ARRAY_SIZE = 100
    random.seed(40)
    original_array = [random.randint(0, 100) for _ in range(ARRAY_SIZE)]

    print(" Task 1: Bubble Sort Two Sides ")
    arr1 = original_array.copy()
    start = time.perf_counter()
    passes, swaps = bubble_sort_two_sides(arr1)
    duration = time.perf_counter() - start
    print(f"Time: {duration:.6f} seconds, Passes: {passes}, Swaps: {swaps}\n")

    print(" Task 2: Merge Sort Without Slicing ")
    arr2 = original_array.copy()
    start = time.perf_counter()
    merge_sort_without_slice(arr2, 0, len(arr2) - 1)
    duration = time.perf_counter() - start
    print(f"Time: {duration:.6f} seconds\n")

    print(" Task 3: Quick Sort with Partition Limits ")
    best_limit = None
    best_time = float('inf')

    for limit in range(2, 15, 2):
        arr3 = original_array.copy()
        start = time.perf_counter()
        quick_sort(arr3, limit)
        duration = time.perf_counter() - start
        print(f"Limit {limit:2}: Time = {duration:.6f} seconds")
        if duration < best_time:
            best_time = duration
            best_limit = limit

    print(f"\nBest limit for quick_sort: {best_limit} (Time: {best_time:.6f} seconds)")