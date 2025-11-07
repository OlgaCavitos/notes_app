from lesson_27 import insert_left


class BinaryTree:
    def __init__(self, value=None):
        self.value = value
        self.left_child= None
        self.right_child = None


    def insert_left(self, value):
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            tree=BinaryTree(value)
            tree.left_child = self.left_child
            self.left_child = tree



    def insert_right(self, value):
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            tree = BinaryTree(value)
            tree.right_child = self.right_child
            self.right_child = tree

    def get_root_value(self):
        return self.value

    def set_root_value(self, value):
        self.value = value

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child


    def _display(self, indent=0, symbol= ' '):
        text=f"{symbol*indent}{self.value}\n"
        text_left=''
        if self.left_child:
            text_left=self.left_child._display(indent=indent+4)
        text_right=''
        if self.right_child:
            text_right=self.right_child._display(indent=indent+4)
        return text+text_left+text_right

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
        # print()


    def pre_order(self):
        print(self.value, end=' ')
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()


if __name__ == "__main__":
    tree = BinaryTree('a')
    tree.insert_left('b')
    tree.insert_right('h')
    # print(tree)
    tree.insert_left('b')
    tree.insert_right('c')
    # print(tree)
    # left=tree.insert_left('b')
    # right =tree.insert_right('c')
    tree.in_order()
    tree.pre_order()
