class BinaryTreeNode:
    def __init__(self, key, left_node=None, right_node=None):
        self.key = key
        self.left_node = left_node
        self.right_node = right_node


    class BinarySearchTree:
        def __init__(self):
            self.root = None

        # @staticmethod


        def add(self, key):
            def _add(key, node):
                if node is None:
                    return BinaryTreeNode(key)
                elif key <= node.key:
                    node.left_node = _add(key,node.left_node)
                else:
                    node.right_node = _add(key,node.right_node)
            self.root=_add(key, self.root)

        def convert_to_list(self):
            def _build_list(container, node):
                if node is not None:
                    if node.left_node is not None:
                        _build_list(container, node.left_node)
                    container.append(node.key)
                    if node.right_node is not None:
                        _build_list(container, node.right_node)
            container=[]
            _build_list(container, self.root)
            return container










