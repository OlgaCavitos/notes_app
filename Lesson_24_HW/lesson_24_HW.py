#Task 1

from stack import Stack

def reverse_text(input_data):
    stack_1 = Stack()

    for char in input_data:
        stack_1.push(char)

    reverse_data=''
    while not stack_1.is_empty():
            reverse_data += stack_1.pop()

    return reverse_data

if __name__ == '__main__':

    assert reverse_text("loop") == "pool"
    assert reverse_text("456") == "654"


#Task2

def balanced_brackets(b: str):
    stack = Stack()
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    def bracket_events(text):
        brackets = {'(': 'open', ')': 'close', '{': 'open', '}': 'close', '[': 'open', ']': 'close'}
        for i, ch in enumerate(text, start=1):
            if ch in brackets:
                yield (brackets[ch], ch, i)

    for event_type, ch, pos in bracket_events(b):
        if event_type == 'open':
            stack.push((ch, pos))
        elif event_type == 'close':
            if stack.is_empty():
                return False
            top_char, top_pos = stack.pop()
            if top_char != bracket_pairs[ch]:
                return False

    if not stack.is_empty():
        return False

    return True

if __name__ == "__main__":

    assert balanced_brackets("([{]})") == False
    assert balanced_brackets("{}()[]") == True


#Task 3

class StackGet(Stack):
    def get_from_stack(self, element):
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
    s = StackGet()

    s.push('x')
    s.push('y')
    assert s.get_from_stack('y') == 'y'
    assert s.pop() == 'x'
    assert s.is_empty()


from queue import Queue

class QueueGet(Queue):
    def get_from_queue(self, element):
        new_queue = Queue()

        while not self.is_empty():
            item=self.dequeue()
            if item == element:
                while not new_queue.is_empty():
                    self.enqueue(new_queue.dequeue())
                return item
            new_queue.enqueue(item)

        while not new_queue.is_empty():
            self.enqueue(new_queue.dequeue())

        raise ValueError(f"Element '{element}' not found in the queue")

if __name__ == '__main__':
    q = QueueGet()

    q.enqueue('x')
    q.enqueue('z')
    q.enqueue('y')
    assert q.get_from_queue('y') == 'y'