# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node’s key.
# The right subtree of a node contains only nodes with keys greater than the node’s key.
# Both the left and right subtrees must also be binary search trees.
# Example :
#
# Input :
#    1
#   /  \
#  2    3
#
# Output : 0 or False
#
#
# Input :
#   2
#  / \
# 1   3
#
# Output : 1 or True
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem


from Level6.Trees.BinaryTree import BinaryTree, Node

INT_MAX = 4294967296
INT_MIN = -4294967296


class Solution:
    def is_bat(self, node):
        return self.is_bst_util(node, INT_MIN, INT_MAX)

    def is_bst_util(self, node, minimum, maximum):
        if node is None:
            return True
        if node.val < minimum or node.val > maximum:
            return False
        return (self.is_bst_util(node.left, minimum, node.val - 1) and
                self.is_bst_util(node.right, node.val + 1, maximum))


A = BinaryTree()
A.insert(100)
res = Solution().is_bat(A.root)
print(res)
