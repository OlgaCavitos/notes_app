#Task 1

class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self.is_empty():
            return self._items.pop()
        else:
            raise IndexError("pop from an empty stack")

if __name__ == '__main__':
    stak_1=Stack()

    input_data=input("Enter some sequence of characters: ")
    for char in input_data:
        stak_1.push(char)

    print("Reverse order sequence of characters:", end=" ")
    while not stak_1.is_empty():
        print(stak_1.pop(), end="")
    print()

print('\n')

#Task2

def check_balanced(b:str):
    stack=[]
    brackets_list={')': '(', '}': '{', ']': '['}

    for i, ch in enumerate(b,start=1):
        if ch in brackets_list.values():
            stack.append((ch,i))
        elif ch in brackets_list:
            if not stack:
                print(f"Unmatched closing '{ch}' at position {i}")
                return False
            top_char, top_index = stack[-1]
            if top_char != brackets_list[ch]:
                print(
                    f"Bracket mismatch at position {i}: expected closing for '{top_char}' "
                    f"from position {top_index}, but got '{ch}'")
                return False
            stack.pop()

    if stack:
        unmatched_char, unmatched_index = stack[-1]
        print(f"Unmatched opening '{unmatched_char}' at position {unmatched_index}")
        return False

    return True

if __name__ == "__main__":
    expression = input("Enter any brackets: ")
    if check_balanced(expression):
        print("The sequence of characters is balanced")
    else:
        print("The sequence of characters is not balanced")


print('\n')

#Task3

class Stack_1:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def size(self):
        return len(self._items)

    def __len__(self):
        return self.size()

    def __str__(self):
        return str(self._items)

    def get_from_stack_1(self, element):
        new_stack = Stack()

        while not self.is_empty():
            item = self.pop()
            if item == element:
                while not new_stack.is_empty():
                    self.push(new_stack.pop())
                return item
            new_stack.push(item)

        while not new_stack.is_empty():
            self.push(new_stack.pop())
        raise ValueError(f"Element '{element}' not found in the stack")


if __name__ == '__main__':
    stack_1=Stack_1()

    stack_1.push('c')
    stack_1.push('a')
    stack_1.push('t')

    print("The stack current data:",stack_1)
    print("The stack current size:", stack_1.size())

    try:
        stack_1.get_from_stack_1('c')
        print("The stack current data:",stack_1)
        print("The stack current size:", stack_1.size())
    except ValueError as e:
        print(e)



