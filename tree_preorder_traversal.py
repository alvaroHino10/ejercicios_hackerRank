class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

# Ordenamiento de arbol en preOrder con recursividad, Preorden:	Raíz → Izquierda → Derecha
def preOrder(root, tree_order):
    # Write your code here
    tree_order.append(root.info)
    if root.left:
        preOrder(root.left, tree_order)
    if root.right:
        preOrder(root.right, tree_order)
    return tree_order

# Metodo con print directo como pedia HackerRank
def preOrder_print(root):
    # Write your code here
    print(''.join(str(root.info)), end=' ')
    if root.left:
        preOrder_print(root.left)
    if root.right:
        preOrder_print(root.right)

if __name__ == '__main__':
    tree = BinarySearchTree()
    t = int(input())

    arr = list(map(int, input().split()))

    for i in range(t):
        tree.create(arr[i])
    order = []
    result = preOrder(tree.root, order)

    print(' '.join(map(str, result)))

