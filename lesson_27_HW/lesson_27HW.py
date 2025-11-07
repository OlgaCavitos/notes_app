#Task 1

class BinaryTree:

    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            tree = BinaryTree(value)
            tree.left_child = self.left_child
            self.left_child = tree
        return self.left_child

    def insert_right(self, value):
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            tree = BinaryTree(value)
            tree.right_child = self.right_child
            self.right_child = tree
        return self.right_child

    def attach_subtree(self, side, subtree):
        if not isinstance(subtree, BinaryTree):
            raise TypeError("subtree must be a BinaryTree instance")
        if side == 'left':
            self.left_child = subtree
        elif side == 'right':
            self.right_child = subtree
        else:
            raise ValueError("side must be 'left' or 'right'")

    def detach_subtree(self, side):
        if side == 'left':
            detached = self.left_child
            self.left_child = None
            return detached
        elif side == 'right':
            detached = self.right_child
            self.right_child = None
            return detached
        else:
            raise ValueError("side must be 'left' or 'right'")

    def get_root_value(self):
        return self.value

    def set_root_value(self, value):
        self.value = value

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def _display(self, indent=0, symbol=' '):
        text = f"{symbol * indent}{self.value}\n"
        if self.left_child:
            text += self.left_child._display(indent=indent + 4)
        if self.right_child:
            text += self.right_child._display(indent=indent + 4)
        return text

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __str__(self):
        return self._display()

    def __repr__(self):
        return f"<BinaryTree: {self.value}>"

    def in_order(self):
        if self.left_child:
            self.left_child.in_order()
        print(self.value, end=' ')
        if self.right_child:
            self.right_child.in_order()

    def pre_order(self):
        print(self.value, end=' ')
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order()
        print(self.value, end=' ')


if __name__ == '__main__':
    root = BinaryTree('X')
    left = root.insert_left('Y')
    right = root.insert_right('Z')
    left.insert_left('O')
    right.insert_right('P')

    print("Initial Tree:")
    print(root)

    subtree = BinaryTree('K')
    subtree.insert_left('L')
    subtree.insert_right('M')

    left.attach_subtree('right', subtree)
    print(root)
    removed = left.detach_subtree('right')
    print(root)
    print(removed)



#Task 2

from html.parser import HTMLParser

class DOM:
    def __init__(self, tag, text=''):
        self.tag = tag
        self.text = text.strip()
        self.child = []

    def add_child(self, node):
        self.child.append(node)

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.root = None

    def handle_starttag(self, tag, attrs):
        node = DOM(tag)
        if self.stack:
            self.stack[-1].add_child(node)
        else:
            self.root = node
        self.stack.append(node)

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1].tag == tag:
            self.stack.pop()

    def handle_data(self, data):
        if data.strip() and self.stack:
            self.stack[-1].text += data.strip()

def search_by_tag(node, tag):
    res = []
    if node.tag == tag and node.text:
        res.append(node.text)
    for child in node.child:
        res.extend(search_by_tag(child, tag))
    return res

if __name__ == "__main__":
    html_doc = """
    <html>
      <body>
        <h1>Title</h1>
        <p>The first part of text.</p>
        <p>The second part of text.</p>
      </body>
    </html>
    """

    parser = MyHTMLParser()
    parser.feed(html_doc)

    matches = search_by_tag(parser.root, 'p')
    print("Text inside <p> tags:", matches)

