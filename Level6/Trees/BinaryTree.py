
# Implementation of BST


class Node:
    def __init__(self, info):  # constructor of class
        self.val = info  # information for node
        self.left = None  # left leef
        self.right = None  # right leef
        self.level = None  # level none defined

    def __str__(self):
        return str(self.val)  # return as string


class BinaryTree:
    def __init__(self):  # constructor of class
        self.root = None

    def insert(self, val):  # create binary search tree nodes
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root
            while 1:
                if val < current.val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.val:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

    def bft(self):  # Breadth-First Traversal
        self.root.level = 0
        queue = [self.root]
        out = []
        current_level = self.root.level
        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node.level > current_level:
                current_level += 1
                out.append("\n")
            out.append(str(current_node.info) + " ")
            if current_node.left:
                current_node.left.level = current_level + 1
                queue.append(current_node.left)
            if current_node.right:
                current_node.right.level = current_level + 1
                queue.append(current_node.right)
            print(''.join(out))

    def in_order(self, node):
        if node is not None:
            self.in_order(node.left)
            print(node.info)
            self.in_order(node.right)

    def pre_order(self, node):
        if node is not None:
            print(node.info)
            self.pre_order(node.left)
            self.pre_order(node.right)

    def post_order(self, node):
        if node is not None:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.info)
