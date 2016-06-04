# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
#
# The first call to next() will return the smallest number in BST.
# Calling next() again will return the next smallest number in the BST, and so on.
#
#  Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
# Try to optimize the additional space complexity apart from the amortized time complexity.


from Level6.Trees.BinaryTree import BinaryTree, Node


class Solution:

    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def has_next(self):
        if len(self.stack) > 0:
            return True
        else:
            return False

    def next(self):
        node = self.stack.pop()
        result = node.val
        if node.right:
            node = node.right
            while node:
                self.stack.append(node)
                node = node.left
        return result


node = Node(2)
node.left = Node(1)
node.right = Node(3)
sol = Solution(node)
while sol.has_next():
    print(sol.next())
