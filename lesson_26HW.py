#Task 1

import time

def binary_search_recursive(arr, target,left, right):    #O(log2 n)
    if left > right:
        return -1
    mid = (left+right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right)


# Fibonacci Search

def fibonacci_search(arr, target):   #O(log n)
    n = len(arr)

    fib=[0,1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])

    offset = -1
    k=len(fib)-1
    while k>1:
        i=min(offset+fib[k-2],n-1)

        if arr[i] < target:
            k-=1
            offset=i
        elif arr[i] > target:
            k-=2
        else:
            return i

    if k>0 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1

    return -1

if __name__ == "__main__":
    arr = list(range(0, 10000))
    target = 9999

    start_time = time.time()
    res_bin = binary_search_recursive(arr, target,0, len(arr)-1)
    end_time = time.time()
    bin_time_ms = (end_time - start_time) * 1000

    print(f"Binary Search found at index {res_bin} in {bin_time_ms:.4f} ms")

    start_time = time.time()
    result_fib = fibonacci_search(arr, target)
    end_time = time.time()
    fib_time_ms = (end_time - start_time) * 1000
    print(f"Fibonacci Search found at index {result_fib} in {fib_time_ms:.4f} ms")



#Task2

    class HashTable:
        def __init__(self, init_size=8):
            self.size = init_size
            self.__resize_container()

        def __resize_container(self):
            self.map = [None] * self.size
            self.order = []

        def _hash(self, key):
            return hash(key) % self.size

        def _resize(self):
            old_map = self.map.copy()
            old_order = self.order.copy()

            self.size *= 2
            self.__resize_container()

            for pos in old_order:
                if old_map[pos] is not None:
                    key, value = old_map[pos]
                    self.add(key, value)

        def _probe(self, pos):
            for i in range(pos + 1, self.size + pos):
                i = i % self.size
                if self.map[i] is None:
                    return i
            return None

        def add(self, key, value):
            pos = self._hash(key)

            if self.map[pos] is None:
                self.map[pos] = (key, value)
                self.order.append(pos)
            elif self.map[pos][0] == key:
                self.map[pos] = (key, value)  # Update existing
            else:
                new_pos = self._probe(pos)
                if new_pos is not None:
                    self.map[new_pos] = (key, value)
                    self.order.append(new_pos)
                else:
                    self._resize()
                    self.add(key, value)

        def get(self, key):
            pos = self._hash(key)
            if self.map[pos] is not None and self.map[pos][0] == key:
                return self.map[pos][1]
            else:
                for i in range(pos + 1, self.size + pos):
                    i = i % self.size
                    if self.map[i] is None:
                        return None
                    if self.map[i][0] == key:
                        return self.map[i][1]
            return None

        def delete(self, key):
            pos = self._hash(key)
            if self.map[pos] is not None and self.map[pos][0] == key:
                self.map[pos] = None
                self.order.remove(pos)
                return
            for i in range(pos + 1, self.size + pos):
                i = i % self.size
                if self.map[i] is None:
                    return
                if self.map[i][0] == key:
                    self.map[i] = None
                    self.order.remove(i)
                    return

        def __len__(self):
            return len(self.order)

        def __contains__(self, key):
            return self.get(key) is not None

        def __str__(self):
            items = []
            for pos in self.order:
                if self.map[pos] is not None:
                    key, value = self.map[pos]
                    items.append(f"{key}: {value}")
            return "{" + ", ".join(items) + "}"


if __name__ == "__main__":
    h = HashTable()
    h.add("x", 1)
    h.add("y", 2)
    h.add("z", 3)

    print(h)
    print(len(h))
    print("y" in h)
    print(h.get("z"))

    h.delete("z")
    print(h)
    print("z" in h)
