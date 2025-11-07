import operator
from binary_tree_1 import BinaryTree

from stack_1 import Stack

class ParseTree(BinaryTree):
    operators={'+': operator.add,
               '-': operator.sub,
               '*': operator.mul,
               }

    def __init__(self, math_exp=''):
        self.exp = math_exp
        self._tree=BinaryTree()
        self._stack=Stack()
        self._stack.push(self._tree)
        if math_exp:
            self.parse()


    @property
    def tree(self):
        return self._tree

    def parse_tree(self):
        #  ( (7 + 3 ) * ( 5 - 2 ) )
        token_list=self.exp.split()
        curr_tree=self._tree
        for token in token_list:
            if token == '(':
                curr_tree.insert_left('')
                self._stack.push(curr_tree)
                curr_tree=curr_tree.get_left_child()
            elif token in ('+', '-', '*', '/'):
                curr_tree.set_root_value(token)
                curr_tree.insert_right('')
                self._stack.push(curr_tree)

            elif token == ')':
                curr_tree=self._stack.pop()
            else:
                curr_tree.set_root_value(int(token))
                curr_tree=self._stack.pop()

        # print(self._tree)

    def evaluate(self, exp=None):
       tree=exp if exp else self._tree
       left_exp=tree.get_left_child()
       right_exp=tree.get_right_child()
       if left_exp and right_exp:
           op=self.operators[tree.get_root_value()]
           return op(self.evaluate(left_exp), self.evaluate(right_exp))
       else:
           return tree.get_root_value()

    def _get_exp(self, tree=None):
        text=''
        if tree:
            text='('+ self._get_exp(tree.left_child) \
                 + str(tree.get_root_value()) \
                 + self._get_exp(tree.right_child) + ')'
        return text

    def print_exp(self, tree=None):
        curr_tree=tree if tree else self._tree
        return self._get_exp(curr_tree)

    def print_exp(self, tree=None):
        curr_tree=tree if tree else self._tree
        return self._get_exp(curr_tree)



if __name__ == "__main__":
    pt=ParseTree("( (7 + 3 ) * ( 5 - 2 ) )")