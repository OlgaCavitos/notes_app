#root    R
#      /  \
#      N   N
#     / \   \
#    L   L   L


my_tree=[
    'a',
        ['b',
           ['d',
               [],
               [],
            ],
         ],
        ]

#print(my_tree)

def binary_tree(r):
    return [r,[],[]]

def insert_left(tree, value):
    tr=tree.pop(1)
    if len(tr)> 1:  #[r, N,[]]->[r, [value,N,[]], []]
        tree.append(1, [value,tr,[]])
    else:           ## [r, [],[]] -> [r, [value, [], []], []]
        tree.insert(1,[value, [], []])


def insert_right(tree, value):
    tr=tree.pop(2)
    if len(tr)> 1:  #[r, N,[]]->[r, [value,N,[]], []]
        tree.append(2, [value,tr,[]])
    else:           ## [r, [],[]] -> [r, [value, [], []], []]
        tree.insert(2,[value, [], []])


def print_tree(tree, indent=0, symbol=' '):
    if len(tree)>1:
        print(f"{symbol*indent}{tree[0]}")
        print_tree(tree[1], indent=indent+4)
        print_tree(tree[2], indent=indent+4)

def get_paths(tree, paths, curr_path):
    curr_path.appned(tree[0])
    if not tree[1] and not tree[2]:
        paths.append(curr_path)
    else:
        if tree[1]:
            get_paths(tree[1], paths, curr_path.copy())
        if tree[2]:
            get_paths(tree[2], paths, curr_path.copy())
    return paths

if __name__ == '__main__':
    tr=binary_tree('a')
    insert_left(tr, 'd')
    insert_right(tr, 'h')

    print(tr)
    print_tree(tr)

