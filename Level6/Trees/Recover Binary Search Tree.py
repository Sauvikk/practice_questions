# Two elements of a binary search tree (BST) are swapped by mistake.
# Tell us the 2 values swapping which the tree will be restored.
#
#  Note:
# A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
# Example :
#
#
# Input :
#          1
#         / \
#        2   3
#
# Output :
#        [1, 2]
#
# Explanation : Swapping 1 and 2 will change the BST to be
#          2
#         / \
#        1   3
# which is a valid BST

from Level6.Trees.BinaryTree import BinaryTree, Node


class Solution:
    def __init__(self):
        self.first = None
        self.prev = None
        self.last = None

    def in_order(self, root):
        if root is None:
            return
        else:
            self.in_order(root.left)
            if self.prev is None:
                self.prev = root
            else:
                if root.val <= self.prev.val:
                    if self.first is None:
                        self.first = self.prev
                    self.last = root
                self.prev = root
            self.in_order(root.right)

    def solution(self, root):
        self.in_order(root)
        # self.first.val, self.last.val = self.last.val, self.first.val
        return [self.last.val, self.first.val]

node = Node(1)
node.left = Node(2)
node.right = Node(3)
res1 = Solution().solution(node)
BinaryTree().in_order(res1)
